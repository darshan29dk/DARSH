@echo off
REM DARSH Dashboard Launcher
REM This script launches the DARSH dashboard

title DARSH Dashboard
echo DARSH Dashboard Launcher
echo =======================
echo Starting dashboard...
echo.

cd /d "c:\DARSH"
python dashboard_launcher.py

echo.
echo Dashboard closed.
pause