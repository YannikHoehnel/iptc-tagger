#!/usr/bin/env python3
"""AI Image Tagger - GUI for writing/checking the IPTC DigitalSourceType tag.

Uses the bundled ExifTool to write the standard IPTC/C2PA
'trainedAlgorithmicMedia' value to the XMP-iptcExt:DigitalSourceType tag,
which is the recognised way to mark an image as AI-generated.

No installation required - just run this script with Python 3
(python3 ai_tagger_gui.py). ExifTool is bundled in the bin/ folder.
"""

import os
import platform
import subprocess
import sys
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

AI_VALUE = "http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia"
TAG = "XMP-iptcExt:DigitalSourceType"

IMAGE_EXTENSIONS = [
    "jpg", "jpeg", "png", "tif", "tiff", "webp", "heic", "heif", "gif", "bmp",
]

if getattr(sys, "frozen", False):
    # Running as a PyInstaller-built executable: use the exe's own folder,
    # not the temp extraction dir, so the sibling bin/ folder is found.
    SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def find_exiftool_command():
    """Return the argv prefix used to invoke the bundled ExifTool."""
    if platform.system() == "Windows":
        exe = os.path.join(SCRIPT_DIR, "bin", "win", "exiftool.exe")
        if os.path.isfile(exe):
            return [exe]
    else:
        script = os.path.join(SCRIPT_DIR, "bin", "mac_linux", "exiftool")
        if os.path.isfile(script):
            perl = "perl"
            return [perl, script]
    # Fall back to a system-wide install, if any.
    return ["exiftool"]


def run_exiftool(args, log):
    cmd = find_exiftool_command() + args
    log(f"$ {' '.join(cmd)}\n")
    try:
        result = subprocess.run(
            cmd,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
    except FileNotFoundError as exc:
        log(f"Could not run ExifTool: {exc}\n")
        return None
    log(result.stdout)
    return result


def ext_args():
    args = []
    for ext in IMAGE_EXTENSIONS:
        args += ["-ext", ext]
    return args


class App:
    def __init__(self, root):
        self.root = root
        self.folder = None
        root.title("AI Image Tagger")
        root.geometry("720x520")
        root.minsize(600, 420)

        top = tk.Frame(root, padx=10, pady=10)
        top.pack(fill="x")

        self.folder_label = tk.Label(
            top, text="No folder selected", anchor="w", fg="#555"
        )
        self.folder_label.pack(fill="x")

        btn_row = tk.Frame(root, padx=10, pady=5)
        btn_row.pack(fill="x")

        tk.Button(
            btn_row, text="1. Select folder...", command=self.select_folder
        ).pack(side="left")

        self.mark_btn = tk.Button(
            btn_row,
            text="2. Mark images as AI-generated",
            command=self.mark_images,
            state="disabled",
        )
        self.mark_btn.pack(side="left", padx=8)

        self.check_btn = tk.Button(
            btn_row,
            text="3. Check images",
            command=self.check_images,
            state="disabled",
        )
        self.check_btn.pack(side="left")

        info = tk.Label(
            root,
            justify="left",
            anchor="w",
            padx=10,
            fg="#555",
            text=(
                "Marking writes the standard IPTC tag DigitalSourceType = "
                "trainedAlgorithmicMedia\nto every image in the selected "
                "folder (including subfolders). This overwrites the files "
                "in place."
            ),
        )
        info.pack(fill="x")

        self.log = scrolledtext.ScrolledText(
            root, state="disabled", wrap="word", padx=8, pady=8
        )
        self.log.pack(fill="both", expand=True, padx=10, pady=10)

        self.status = tk.Label(root, text="Ready", anchor="w", padx=10)
        self.status.pack(fill="x")

    def log_write(self, text):
        def _write():
            self.log.configure(state="normal")
            self.log.insert("end", text)
            self.log.see("end")
            self.log.configure(state="disabled")

        self.root.after(0, _write)

    def clear_log(self):
        self.log.configure(state="normal")
        self.log.delete("1.0", "end")
        self.log.configure(state="disabled")

    def set_busy(self, busy, message=""):
        state = "disabled" if busy else "normal"
        self.mark_btn.configure(state=state)
        self.check_btn.configure(state=state)
        self.status.configure(text=message or ("Working..." if busy else "Ready"))

    def select_folder(self):
        folder = filedialog.askdirectory(title="Select folder with images")
        if not folder:
            return
        self.folder = folder
        self.folder_label.configure(text=f"Folder: {folder}")
        self.mark_btn.configure(state="normal")
        self.check_btn.configure(state="normal")

    def mark_images(self):
        if not self.folder:
            return
        if not messagebox.askyesno(
            "Mark images as AI-generated",
            "This will write the AI-generated source tag to every image "
            f"in:\n\n{self.folder}\n\n(including subfolders), overwriting "
            "the files in place.\n\nContinue?",
        ):
            return
        self.clear_log()
        self.set_busy(True, "Marking images...")
        threading.Thread(target=self._mark_worker, daemon=True).start()

    def _mark_worker(self):
        args = (
            ["-r", "-overwrite_original", f"-{TAG}={AI_VALUE}"]
            + ext_args()
            + [self.folder]
        )
        result = run_exiftool(args, self.log_write)
        if result is not None:
            self.log_write("\nDone.\n")
        self.root.after(0, lambda: self.set_busy(False))

    def check_images(self):
        if not self.folder:
            return
        self.clear_log()
        self.set_busy(True, "Checking images...")
        threading.Thread(target=self._check_worker, daemon=True).start()

    def _check_worker(self):
        args = (
            ["-r", "-T", "-Filename", f"-{TAG}"] + ext_args() + [self.folder]
        )
        cmd = find_exiftool_command() + args
        try:
            result = subprocess.run(
                cmd,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
        except FileNotFoundError as exc:
            self.log_write(f"Could not run ExifTool: {exc}\n")
            self.root.after(0, lambda: self.set_busy(False))
            return

        lines = [l for l in result.stdout.splitlines() if l.strip()]
        marked, unmarked, other = [], [], []
        for line in lines:
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            name, value = parts[0], parts[1]
            if value == AI_VALUE:
                marked.append(name)
            elif value in ("-", ""):
                unmarked.append(name)
            else:
                other.append((name, value))

        total = len(marked) + len(unmarked) + len(other)
        self.log_write(
            f"Checked {total} image(s) in {self.folder}\n"
            f"  Marked as AI-generated: {len(marked)}\n"
            f"  Not marked: {len(unmarked)}\n"
            f"  Marked with a different value: {len(other)}\n\n"
        )
        for name in marked:
            self.log_write(f"[AI]      {name}\n")
        for name, value in other:
            self.log_write(f"[OTHER]   {name}  (DigitalSourceType={value})\n")
        for name in unmarked:
            self.log_write(f"[not set] {name}\n")

        self.root.after(0, lambda: self.set_busy(False))


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
