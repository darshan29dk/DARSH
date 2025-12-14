# DARSH - Local-first Personal Windows AI Agent

DARSH is a free, local-first personal Windows AI agent built in Python.
It provides an always-listening wake-word, local speech-to-text, screen understanding (OCR), UI automation, scheduling, permissions, and a system tray UI.

This repository is a complete implementation designed for local use and production deployment.

See `requirements.txt` for dependencies and `main.py` for the entry point.

Important: Some features require installing optional native binaries (Tesseract OCR, Playwright browsers, pocketsphinx for offline wake-word). See notes below.

## Features

- **Voice Control**: Always-on microphone with wake word detection ("Hey JARVIS", "Hey FRIDAY")
- **Speech-to-Text**: Local transcription using Whisper/faster-whisper
- **Voice Feedback**: Spoken responses to confirm actions and provide status updates
- **Screen Understanding**: OCR-based screen analysis and UI element detection
- **UI Automation**: Control any Windows application via mouse/keyboard actions
- **Web Automation**: Browser automation using Playwright
- **Task Scheduling**: Daily routines with cron-like syntax
- **Conditional Triggers**: Event-based automation (battery level, network status, etc.)
- **Plugin System**: Extensible architecture for custom functionality
- **Dashboard**: Graphical interface for monitoring and configuration
- **Self-Healing**: Automatic retry mechanisms for failed actions
- **Security**: Local execution with permission controls and emergency stop
- **System Tray**: Minimal UI with auto-start capability

## Quick Start (Developer)

1. Create and activate a Python 3.10+ venv.
2. Install requirements:
```powershell
python -m pip install -r requirements.txt
# If using Playwright:
python -m playwright install
```
3. Install Tesseract (Windows): download from https://github.com/tesseract-ocr/tesseract and ensure `tesseract.exe` is on PATH.
4. (Optional) Install Ollama locally if you want a local LLM backend: https://ollama.com
5. Run DARSH (development):
```powershell
python main.py
```

## Installation Script

For easier setup, use the installation script:
```powershell
python setup/install.py
```

This script will:
- Install all Python dependencies
- Install Playwright browsers
- Check for Tesseract OCR installation
- Create a desktop shortcut

## Packaging

Use PyInstaller to build a Windows exe. A helper script is included: `setup/pyinstaller_build.ps1`.

Example (PowerShell):
```powershell
.\setup\pyinstaller_build.ps1
```

## Auto-start on Boot

DARSH can be configured to start automatically when you log into Windows:
1. Run DARSH at least once
2. Right-click the DARSH icon in the system tray
3. Select "Auto-start" to enable/disable auto-start

## Daily Routines

DARSH supports scheduled tasks with the following commands:
- `click:text` - Click on UI element with specified text
- `click_any:label1,label2` - Click on first available element from list
- `type:text` - Type specified text
- `shortcut:ctrl+c` - Press keyboard shortcut
- `wait_for:text` - Wait for text to appear on screen
- `open_url:https://example.com` - Open URL in browser

Example routines:
- "Every day at 9 AM open browser and check mail"
- "Every night at 10 PM organize downloads and shut down"

## Conditional Triggers

DARSH supports event-based automation:
- **Battery Level**: Trigger when battery drops below a threshold
- **Network Status**: Trigger when connecting to/disconnecting from network
- **CPU/Memory Usage**: Trigger when system resources exceed thresholds
- **Process Detection**: Trigger when specific applications start/stop

## Plugin System

Extend DARSH functionality with custom plugins:
- Place `.py` files in the `plugins/` directory
- Plugins can register custom actions
- Template plugin included for reference

## Dashboard

Access detailed monitoring and configuration through the dashboard:
1. Right-click the DARSH icon in the system tray
2. Select "Dashboard"
3. View logs, statistics, and configure settings

## Security & Privacy

- Local-first: no cloud services are required or enabled by default.
- No continuous audio recording or continuous screen video.
- Screenshots are kept in memory and discarded immediately after OCR.
- Capability-based permissions for sensitive actions.
- Emergency stop mechanism to halt all operations.

## Architecture

```
DARSH/
├── brain/          # AI processing (Ollama integration)
├── executor/       # UI automation actions
├── memory/         # SQLite database for persistence
├── plugins/        # Extension modules
├── scheduler/      # Task scheduling and triggers
├── security/       # Permission management
├── setup/          # Installation and packaging scripts
├── ui/             # System tray and dashboard interface
├── utils/          # Logging and utility functions
├── vision/         # Screen understanding and OCR
└── voice/          # Voice recognition and wake word
```

## License

MIT