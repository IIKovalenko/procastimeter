#coding: utf-8
from pync import Notifier
from mysql import create_db_connection
import settings


def show_procastination_warning():
    today_procastinated_min = get_today_procastion_time()
    Notifier.notify(
        'Procastinated %s min\n(%.2d%% from today max)' % (
            today_procastinated_min,
            float(today_procastinated_min) / settings.MAX_PROCASTINATION_TIME_DAY_MIN * 100
        ),
        title='Procastimeter',
    )


def get_today_procastion_time():
    data = get_statistics(time_from_now_days=1)
    return data['total_procastinated_time']


def print_week_statistics():
    """ Calculates week statistics and shows ti to stdout"""
    data = get_statistics(time_from_now_days=7)
    show_statistics_to_stdout(data)


def get_statistics(time_from_now_days=7, processed=True):
    db = create_db_connection()
    cursor = db.cursor()
    cursor.execute(
        '''SELECT is_work_page, COUNT(*) as amount
           FROM browser_data
           WHERE timestamp BETWEEN date_sub(now(), INTERVAL %s DAY) and now()
           GROUP BY is_work_page;
        ''',
        (time_from_now_days,)
    )
    raw_data = cursor.fetchall()
    db.close()
    return process_raw_data(raw_data) if processed else raw_data


def process_raw_data(raw_data):
    if raw_data:
        data = {d[0]: d[1] * settings.SLEEP_TIME_SECONDS / 60 for d in raw_data}
    else:
        data = {0: 0, 1: 0}
    return {
        'total_logged': sum(data.values()),
        'total_work_time': data[1],
        'total_procastinated_time': data[0],
    }


def show_statistics_to_stdout(data):
    print "WEEK STATISTICS\n\nTotal logged: %s min\n\tWork time: %s min\n\tProcastinated: %s min" % (
        data['total_logged'],
        data['total_work_time'],
        data['total_procastinated_time'],
    )


if __name__ == "__main__":
    print_week_statistics()
