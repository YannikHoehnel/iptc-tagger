#!/bin/bash
cd "$(dirname "$0")"

if command -v python3 >/dev/null 2>&1; then
    python3 ai_tagger_gui.py
else
    echo "Python 3 was not found on this computer."
    echo "Install it once from https://www.python.org/downloads/macos/"
    echo "(or run 'xcode-select --install' in Terminal), then run this file again."
    read -p "Press Enter to close this window..."
fi
