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

Double-click "AI Image Tagger.exe" to start.

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
