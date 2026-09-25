AI Image Tagger
===============

This little tool marks images as AI-generated using the official IPTC
metadata field (DigitalSourceType = "trainedAlgorithmicMedia"). This is
the standard, industry-recognised tag - most photo/DAM tools and platforms
that check for AI content will read it.

It also lets you check whether images already have that tag.

How to start it
----------------
Download the zip for your OS from the project's GitHub Releases page and
unzip it. No Python install needed - everything required is bundled.

Windows : double-click "AI Image Tagger.exe"
Mac     : double-click "AI Image Tagger.app"
          (first time: right-click it and choose "Open" if macOS warns
          about an unidentified developer)
Linux   : double-click "AI Image Tagger" (or run it from a terminal:
          ./"AI Image Tagger")

Keep the app next to its "bin" folder - that's where the bundled
ExifTool lives.

Running from source (developers)
---------------------------------
If you'd rather run the Python script directly instead of the packaged
app, you need Python 3 installed:
Windows : double-click "Start-AI-Tagger-Windows.bat"
Mac     : double-click "Start-AI-Tagger-Mac.command"
Linux   : double-click "Start-AI-Tagger-Linux.sh" (or run it from a
          terminal: ./Start-AI-Tagger-Linux.sh)

Linux only: if the window doesn't open, you may need the Tk package:
  sudo apt install python3-tk

How to use it
-------------
1. Click "Select folder..." and choose the folder with your images
   (subfolders are included automatically).
2. Click "Mark images as AI-generated" to write the tag to every image
   in that folder. This overwrites the files in place (no backup copies
   are kept).
3. Click "Check images" at any time to see which images already carry
   the AI tag, which don't, and which have some other value set.

Supported file types: jpg, jpeg, png, tif, tiff, webp, heic, heif, gif, bmp

What it does under the hood
----------------------------
The tool bundles ExifTool (the well-known, open-source metadata tool -
https://exiftool.org) and simply runs it for you:

  exiftool -r -overwrite_original -XMP-iptcExt:DigitalSourceType=^
    http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia ^
    <folder>

No files ever leave your computer - everything runs locally.
