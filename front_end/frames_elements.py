from selene import query
from selene.support import by
from selene.support.shared import browser


class BasePageElements:
    frames_link = "Frames"
    nexted_frames_link = "Nested Frames"


class NestedFramesElements:
    frame = "frame"
    frame_top = "frame-top"
    frame_bottom = "frame-bottom"
    frame_middle = "frame-middle"
    frame_left = "frame-left"
    frame_right = "frame-right"


def select_page(page_to_select):
    browser.element(by.link_text(page_to_select)).click()


def print_frame_text(position):
    return browser.element(by.text(position)).get(query.text)


def switch_to_frame(frame_to_switch):
    browser.switch_to.frame(frame_to_switch)


def switch_to_parents_frame(frames_level: int = 1):
    for level in range(frames_level):
        browser.switch_to.parent_frame()
