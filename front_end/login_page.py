from selene import be
from selene.support.shared import browser


class LoginPageElements:
    email = "//input[@type='email']"
    password = "//input[@type='password']"
    log_in_button = "//button[@type='submit']"
    incorrect_email_pass = "//div[text()='Incorrect email or password']"


def input_login(username, password):
    browser.element(LoginPageElements.email).set(username)
    browser.element(LoginPageElements.password).set(password)


def click_submit():
    browser.element(LoginPageElements.log_in_button).click()


def check_submit_button_enabled():
    return browser.element(LoginPageElements.log_in_button).should(be.enabled)


def check_submit_button_disabled():
    return browser.element(LoginPageElements.log_in_button).should(be.disabled)


def check_validation_message_appears():
    return browser.element(LoginPageElements.incorrect_email_pass).should(be.visible)
