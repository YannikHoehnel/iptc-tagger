@echo off
setlocal
set SCRIPT_DIR=%~dp0

where pythonw >nul 2>nul
if %errorlevel%==0 (
    start "" pythonw "%SCRIPT_DIR%ai_tagger_gui.py"
    goto :eof
)

where python >nul 2>nul
if %errorlevel%==0 (
    start "" python "%SCRIPT_DIR%ai_tagger_gui.py"
    goto :eof
)

echo Python was not found on this computer.
echo.
echo Please install Python once from https://www.python.org/downloads/
echo During setup, make sure to tick "Add python.exe to PATH".
echo Then double-click this file again.
pause
