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

Double-click "AI Image Tagger.app" to start - see "First time on a Mac"
below, macOS will block it once before you can open it.

Keep it next to its "bin" folder - that's where the bundled ExifTool
lives.

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
