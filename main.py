"""DARSH main entry point.

Starts the tray UI, DB, scheduler, and wake-listener. This file coordinates modules.
"""
import time
import threading
from memory import db
from utils import logger
from ui.tray import TrayApp
from scheduler import scheduler
from voice.wake import WakeListener
from voice.assistant import Assistant
from security import permissions
from brain import ollama_client
from core import controller
from plugins import initialize_plugins


def on_wake(wake_word: str):
    logger.info('main', 'wake_detected', wake_word)
    # For MVP, just log. In production, this would activate a STT + brain pipeline.


def main():
    # initialize DB
    db.init_db()
    
    # initialize plugins
    initialize_plugins()

    # start UI tray
    tray = TrayApp()
    tray.start()

    # start scheduler
    scheduler.start_scheduler()

    # assistant and wake listener
    assistant = Assistant()
    wake = WakeListener(assistant.on_wake)
    # register with controller so UI can pause/resume auto-pickup
    controller.set_wake_listener(wake)
    wake.start()

    logger.info('main', 'started', 'DARSH is now running and listening for wake words')

    try:
        while True:
            # check emergency stop
            if permissions.is_emergency_stopped():
                logger.info('main', 'stopped', 'emergency_stop_active')
                break
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info('main', 'interrupted', 'user_requested_shutdown')
    except Exception as e:
        logger.info('main', 'error', str(e))
    finally:
        logger.info('main', 'shutdown', 'DARSH has been shut down')


if __name__ == '__main__':
    main()