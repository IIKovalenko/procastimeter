"""
    Daemon for poor people.
    Usage: nohup python activity_daemon.py &
"""
from time import sleep
from browser_spy import log_active_browser_tab
import settings
from statistics import show_procastination_warning


if __name__ == "__main__":
    counter = 0
    notifications_interval = settings.NOTIFICATION_INTERVAL_MIN / (settings.SLEEP_TIME_SECONDS / 60)
    while True:
        if settings.SHOW_NOTIFICATION and not counter % notifications_interval:
            show_procastination_warning()
        log_active_browser_tab()
        sleep(settings.SLEEP_TIME_SECONDS)
        counter += 1
