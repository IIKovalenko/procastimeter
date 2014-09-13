PROCASTIMETER
=============


Tool for logging and measuring working activity (only active browser tab for now).

Checks if current tab is considered as work-related tab and saves the data to MySQL database.


Requirements
------------

MacOS only for now.


Usage
-----

`activity_daemon.py` runs infinite loop with logging action.

Sample usage:

    WASTE_URL_PARTS='["vk.com", "pikabu.ru"]' python activity_daemon.py

`statistics.py` get week statistics and prints it to stdout.

Sample output:

    WEEK STATISTICS

    Total logged: 17 min
        Work time: 8 min
        Procastinated: 9 min

Configuration
-------------

All configurations values are stored as environment variables.

* `DEBUG` - turns on debug output, etc.

* `SLEEP_TIME_SECONDS` - period of logging

* `DB_NAME, DB_USER, DB_PASSWORD` - database access.

* `BROWSER_APP_NAME` - process name of browser app. Default - 'Google Chrome'.

* `WASTE_URL_PARTS` - JSON list of bad url patterns. If they are found, page considered as work-unrelated.
