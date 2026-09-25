#!/bin/bash
cd "$(dirname "$0")"

if command -v python3 >/dev/null 2>&1; then
    python3 ai_tagger_gui.py
else
    echo "Python 3 was not found. Install it via your package manager, e.g.:"
    echo "  sudo apt install python3 python3-tk"
    read -p "Press Enter to close this window..."
fi
