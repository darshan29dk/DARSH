@echo off
echo DARSH Setup Script
echo ==================

echo Installing Python dependencies...
pip install -r requirements.txt

echo Installing Playwright browsers...
python -m playwright install

echo Setup complete!
echo.
echo To run DARSH, use: python main.py
echo.
pause