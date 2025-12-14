#!/usr/bin/env python3
"""
Script to launch the DARSH dashboard directly.
"""

from ui.dashboard import show_dashboard
import time

if __name__ == "__main__":
    print("Launching DARSH Dashboard...")
    show_dashboard()
    print("Dashboard launched. Keeping script alive for 30 seconds...")
    time.sleep(30)
    print("Script ending...")