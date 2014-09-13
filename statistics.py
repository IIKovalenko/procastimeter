#coding: utf-8
from mysql import create_db_connection
import settings


def print_week_statistics():
    """ Calculates week statistics and shows ti to stdout"""
    data = process_raw_data(get_statistics())
    show_statistics_to_stdout(data)


def get_statistics(time_from_now_days=7):
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
    return raw_data


def process_raw_data(raw_data):
    data = {d[0]: d[1] * settings.SLEEP_TIME_SECONDS / 60 for d in raw_data}
    return {
        'total_logged': sum(data.values()),
        'total_work_time': data[1],
        'total_procastinated_time': data[0],
    }


def show_statistics_to_stdout(data):
    print "WEEK STATISTICS.\n\nTotal logged: %s min\n\tWork time: %s min\n\tProcastinated: %s min" % (
        data['total_logged'],
        data['total_work_time'],
        data['total_procastinated_time'],
    )


if __name__ == "__main__":
    print_week_statistics()
