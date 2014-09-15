#coding: utf-8
import urlparse
import appscript
from mysql import save_page_data_to_mysql, get_host_info
import settings


def log_active_browser_tab():
    """
        Gets active browser tab and saves it to database
    """
    page_data = get_active_tab_data()
    save_page_data_to_mysql(page_data)


def get_active_tab_data():
    """
        Return Google Chrome's active tab name and url.
        Mac OS only.
    """
    window_num = 0  # assume there is only window FIXME
    browser_window = appscript.app(settings.BROWSER_APP_NAME).windows[window_num]
    active_tab_index = browser_window.active_tab_index() - 1  # zero-based
    active_tab = browser_window.tabs()[active_tab_index]
    data = {
        'title': active_tab.title(),
        'url': active_tab.URL(),
    }
    data['is_work_page'] = is_appropriate_page(data)
    return data


def is_appropriate_page(page_data):
    """
        Return True if page considered as working page
    """
    host = urlparse.urlparse(page_data['url'])[1]
    host_info = get_host_info(host)
    return host_info['is_work_host'] if host_info else False