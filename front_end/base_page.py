from selene.support.shared import browser


class BasePageElements:
    login_tab = "//span[text()='Login']"
    smart_slides = "//a[@title='Log in to SmartSlides']"


def select_login_tab():
    browser.element(BasePageElements.login_tab).click()
    browser.element(BasePageElements.smart_slides).click()
