from selene import query
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


class DynamicLoadElements:
    start_button = "Start"
    loading = "loading"
    finish = "finish"


def click_start_button():
    browser.element(by.text(DynamicLoadElements.start_button)).click()


def wait_loading_complete():
    browser.element(by.id(DynamicLoadElements.loading)).with_(timeout=10).wait_until(be.hidden)


def print_console_text():
    return browser.element(by.id(DynamicLoadElements.finish)).get(query.text)
