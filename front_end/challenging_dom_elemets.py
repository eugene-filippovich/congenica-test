from selene import be, by, query
from selene.support.shared import browser


class ChallengingDomElements:
    main_table = "//div[@class='large-10 columns']"
    table_rows = "//div[@class='large-10 columns']//tr"
    qux_button = "qux"


def get_header_index(headers, header_to_find):
    headers_list = browser.elements(by.xpath(headers))[0].text.split(" ")
    header_index = headers_list.index(header_to_find)
    return header_index


def find_selected_row(table, cell_to_find: str):
    for row in browser.elements(by.xpath(table)):
        if cell_to_find in row.get(query.text):
            return row


def highlight_inner_element(main_element, inner_element: int, td_index: int):
    browser.elements(by.xpath(main_element))[inner_element].elements("td")[td_index].execute_script(
        "arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');")


def unhighlight_inner_element(main_element, inner_element: int, td_index: int):
    browser.elements(by.xpath(main_element))[inner_element].elements("td")[td_index].execute_script(
        "arguments[0].setAttribute('style', 'none');")


def highlight_text(element, button):
    element.element(by.text(button)).execute_script(
        "arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');")


def unhighlight_text(element, button):
    element.element(by.text(button)).execute_script(
        "arguments[0].setAttribute('style', 'none');")


def click_button(button_name):
    browser.element(by.text(button_name)).click()
