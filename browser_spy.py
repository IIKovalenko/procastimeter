#coding: utf-8
import appscript
from mysql import save_page_data_to_mysql
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
    return any([keyword in page_data['url'] for keyword in settings.WASTE_URL_PARTS])
