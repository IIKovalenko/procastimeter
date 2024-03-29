# coding: utf-8
import json
import os


DEBUG = False

SLEEP_TIME_SECONDS = 60
MAX_PROCASTINATION_TIME_DAY_MIN = 120

SHOW_NOTIFICATION = True
NOTIFICATION_INTERVAL_MIN = 10

DB_NAME = os.environ.get('DB_NAME', 'procastimeter')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')

BROWSER_APP_NAME = os.environ.get('BROWSER_APP_NAME', 'Google Chrome')
