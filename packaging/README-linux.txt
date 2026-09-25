AI Image Tagger
===============

This little tool marks images as AI-generated using the official IPTC
metadata field (DigitalSourceType = "trainedAlgorithmicMedia"). This is
the standard, industry-recognised tag - most photo/DAM tools and platforms
that check for AI content will read it.

It also lets you check whether images already have that tag.

How to start it
----------------
No installation needed - everything required is bundled.

Double-click "AI Image Tagger" to start (or run it from a terminal:
./"AI Image Tagger").

Keep it next to its "bin" folder - that's where the bundled ExifTool
lives.

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

Dieses kleine Tool markiert Bilder als KI-generiert, indem es das
offizielle IPTC-Metadatenfeld verwendet (DigitalSourceType =
"trainedAlgorithmicMedia"). Das ist der Standard-Tag, der von den
meisten Foto-/DAM-Tools und Plattformen zur KI-Erkennung ausgelesen wird.

Außerdem kannst du damit prüfen, ob Bilder diesen Tag bereits gesetzt
haben.

Wie du es startest
-------------------
Keine Installation nötig - alles Notwendige ist bereits enthalten.

Doppelklicke auf "AI Image Tagger", um es zu starten (oder führe es im
Terminal aus: ./"AI Image Tagger").

Lasse es neben dem Ordner "bin" liegen - dort befindet sich das
mitgelieferte ExifTool.

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
