"""
    Daemon for poor people.
    Usage: nohup python activity_daemon.py &
"""
from time import sleep
from browser_spy import log_active_browser_tab
import settings


if __name__ == "__main__":
    while True:
        log_active_browser_tab()
        sleep(settings.SLEEP_TIME_SECONDS)
