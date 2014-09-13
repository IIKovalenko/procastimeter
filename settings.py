# coding: utf-8
import json
import os


DEBUG = False

SLEEP_TIME_SECONDS = 60

DB_NAME = os.environ.get('DB_NAME', 'procastimeter')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')

BROWSER_APP_NAME = os.environ.get('BROWSER_APP_NAME', 'Google Chrome')

# If any of this list found in page url, then page considered as pocastinating
WASTE_URL_PARTS = json.loads(os.environ.get('WASTE_URL_PARTS', '[]'))
