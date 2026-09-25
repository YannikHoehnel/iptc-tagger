AI Image Tagger
===============

Note: this is the full developer/source README, covering every platform.
The Windows/macOS/Linux release zips each ship a trimmed README.txt with
only the instructions for that platform (see packaging/README-*.txt).

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
Mac     : double-click "AI Image Tagger.app" - see "First time on a Mac"
          below, macOS will block it once before you can open it
Linux   : double-click "AI Image Tagger" (or run it from a terminal:
          ./"AI Image Tagger")

Keep the app next to its "bin" folder - that's where the bundled
ExifTool lives.

First time on a Mac
--------------------
The app isn't notarized by Apple, so macOS blocks it the first time with
a warning like "Apple could not verify that this app is free of malware".
This is normal and only needs to be done once per Mac:

1. Try to open "AI Image Tagger.app" - you'll get the warning. Click
   "Done" (not "Move to Trash").
2. Open System Settings > Privacy & Security.
3. Scroll down to the Security section. You'll see a message that
   "AI Image Tagger" was blocked, with an "Open Anyway" button next to
   it. Click it (enter your Mac password/Touch ID if asked).
4. Open the app again. A second, smaller dialog appears - this one has
   an "Open" button. Click it.

After this one-time confirmation, the app opens normally from then on.

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


================================================================
Deutsch
================================================================

Hinweis: Dies ist die vollständige Entwickler-/Quellcode-README für alle
Plattformen. Die Windows-/macOS-/Linux-Release-ZIPs enthalten jeweils
eine gekürzte README.txt mit nur den Anweisungen für die jeweilige
Plattform (siehe packaging/README-*.txt).

Dieses kleine Tool markiert Bilder als KI-generiert, indem es das
offizielle IPTC-Metadatenfeld verwendet (DigitalSourceType =
"trainedAlgorithmicMedia"). Das ist der Standard-Tag, der von den
meisten Foto-/DAM-Tools und Plattformen zur KI-Erkennung ausgelesen wird.

Außerdem kannst du damit prüfen, ob Bilder diesen Tag bereits gesetzt
haben.

Wie du es startest
-------------------
Lade das ZIP für dein Betriebssystem von der GitHub-Releases-Seite des
Projekts herunter und entpacke es. Keine Python-Installation nötig -
alles Notwendige ist bereits enthalten.

Windows : Doppelklick auf "AI Image Tagger.exe"
Mac     : Doppelklick auf "AI Image Tagger.app" - siehe "Beim ersten
          Start auf einem Mac" weiter unten, macOS blockiert die App
          einmalig, bevor du sie öffnen kannst
Linux   : Doppelklick auf "AI Image Tagger" (oder im Terminal ausführen:
          ./"AI Image Tagger")

Lasse die App neben dem Ordner "bin" liegen - dort befindet sich das
mitgelieferte ExifTool.

Beim ersten Start auf einem Mac
--------------------------------
Die App ist nicht von Apple notarisiert, daher blockiert macOS sie beim
ersten Start mit einer Warnung wie "Apple konnte nicht überprüfen, ob
diese App frei von Schadsoftware ist". Das ist normal und muss nur
einmal pro Mac gemacht werden:

1. Versuche, "AI Image Tagger.app" zu öffnen - du bekommst die Warnung
   angezeigt. Klicke auf "Fertig" (nicht auf "In den Papierkorb legen").
2. Öffne die Systemeinstellungen > Datenschutz & Sicherheit.
3. Scrolle nach unten zum Bereich "Sicherheit". Dort siehst du einen
   Hinweis, dass "AI Image Tagger" blockiert wurde, mit einem Button
   "Trotzdem öffnen" daneben. Klicke darauf (gib bei Bedarf dein
   Mac-Passwort ein oder nutze Touch ID).
4. Öffne die App erneut. Es erscheint ein zweites, kleineres Fenster -
   dieses hat einen "Öffnen"-Button. Klicke darauf.

Nach dieser einmaligen Bestätigung startet die App danach ganz normal.

Aus dem Quellcode ausführen (Entwickler)
------------------------------------------
Wenn du lieber das Python-Skript direkt ausführen möchtest statt der
gepackten App, benötigst du Python 3:
Windows : Doppelklick auf "Start-AI-Tagger-Windows.bat"
Mac     : Doppelklick auf "Start-AI-Tagger-Mac.command"
Linux   : Doppelklick auf "Start-AI-Tagger-Linux.sh" (oder im Terminal
          ausführen: ./Start-AI-Tagger-Linux.sh)

Nur Linux: Falls sich das Fenster nicht öffnet, brauchst du eventuell
das Tk-Paket:
  sudo apt install python3-tk

Wie du es benutzt
------------------
1. Klicke auf "Select folder..." und wähle den Ordner mit deinen Bildern
   aus (Unterordner werden automatisch einbezogen).
2. Klicke auf "Mark images as AI-generated", um den Tag in jedes Bild
   in diesem Ordner zu schreiben. Dies überschreibt die Dateien direkt
   (es werden keine Sicherungskopien angelegt).
3. Klicke jederzeit auf "Check images", um zu sehen, welche Bilder den
   KI-Tag bereits tragen, welche nicht, und welche einen anderen Wert
   gesetzt haben.

Unterstützte Dateitypen: jpg, jpeg, png, tif, tiff, webp, heic, heif,
gif, bmp

Was im Hintergrund passiert
-----------------------------
Das Tool bringt ExifTool mit (das bekannte Open-Source-Metadaten-Tool -
https://exiftool.org) und ruft es einfach für dich auf:

  exiftool -r -overwrite_original -XMP-iptcExt:DigitalSourceType=^
    http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia ^
    <Ordner>

Es verlassen keine Dateien deinen Computer - alles läuft lokal.
