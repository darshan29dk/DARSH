#!/usr/bin/env python3
"""
Standalone launcher for the DARSH dashboard.
"""

import sys
import os
import threading
import time

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from ui.dashboard import Dashboard

def main():
    """Main function to launch the dashboard."""
    print("DARSH Dashboard Launcher")
    print("========================")
    print("Initializing dashboard...")
    
    # Create and show dashboard
    dashboard = Dashboard()
    
    print("Dashboard initialized.")
    print("Launching GUI...")
    print("Close the dashboard window to exit.")
    
    # Show the dashboard (this will block until window is closed)
    dashboard.show()
    
    print("Dashboard closed. Exiting...")

if __name__ == "__main__":
    main()