from selene import be
from selene.support.shared import browser


class SmartSlidesPageElements:
    new_element_hint = "div.cdk-overlay-pane"


def new_slideshow_element_hint():
    return browser.element(SmartSlidesPageElements.new_element_hint).should(be.disabled).text
