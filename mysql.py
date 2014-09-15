#coding: utf-8
from datetime import datetime
import MySQLdb
import settings


def save_page_data_to_mysql(page_data, timestamp=None):
    timestamp == timestamp or datetime.now()
    execute_single_db_query(
        'INSERT INTO browser_data (timestamp, page_title, page_url, is_work_page) VALUES (%s, %s, %s, %s)',
        (timestamp, page_data['title'], page_data['url'], page_data['is_work_page'])
    )  # TODO check if insert failed


def create_db_table():
    execute_single_db_query(
        """
            CREATE TABLE browser_data (
                timestamp TIMESTAMP,
                page_title CHAR(255),
                page_url CHAR(255),
                is_work_page BOOLEAN
            );
            CREATE TABLE host_data (
              host CHAR(255),
              is_work_host BOOLEAN,
              category CHAR(255)
            );
        """
    )


def get_host_info(host_name, create_nonexisting=True):
    db = create_db_connection()
    cursor = db.cursor()
    cursor.execute(
        'SELECT host, is_work_host FROM host_data WHERE host=%s;',
        (host_name,)
    )
    raw_data = cursor.fetchall()
    if create_nonexisting and not raw_data:
        execute_single_db_query(
            'INSERT INTO host_data (host, is_work_host) VALUES (%s, %s)',
            (host_name, None)
        )
    db.close()
    if raw_data and raw_data[0][1]:
        return {
            'host': raw_data[0][0],
            'is_work_host': raw_data[0][1],
        }
    else:
        return None


def execute_single_db_query(query, query_args=None, commit_required=True):
    db = create_db_connection()
    query_result = db.cursor().execute(query, query_args or ())
    if settings.DEBUG:
        print('QUERY: %s\n RESULT: %s\n' % (query, query_result))
    if commit_required:
        db.commit()
    db.close()


def create_db_connection():
    return MySQLdb.connect(
        host="localhost",
        user=settings.DB_USER,
        passwd=settings.DB_PASSWORD,
        db=settings.DB_NAME
    )
