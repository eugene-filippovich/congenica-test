import time

import pytest

from front_end import challenging_dom_elemets
from front_end.challenging_dom_elemets import ChallengingDomElements


class TestTaskThree:
    definiebas7 = "Definiebas7"
    iuvaret7 = "Iuvaret7"

    @pytest.fixture(scope='class')
    def base_url(self):
        yield "http://the-internet.herokuapp.com/challenging_dom"

    def test_highlight_elements(self):
        header_index = challenging_dom_elemets.get_header_index(ChallengingDomElements.table_rows, "Diceret")
        challenging_dom_elemets.highlight_inner_element(ChallengingDomElements.table_rows, 3, header_index)
        time.sleep(1)
        challenging_dom_elemets.unhighlight_inner_element(ChallengingDomElements.table_rows, 3, header_index)
        time.sleep(1)

        raw_with_delete = challenging_dom_elemets.find_selected_row(ChallengingDomElements.table_rows, "Apeirian7")
        challenging_dom_elemets.highlight_text(raw_with_delete, "delete")
        time.sleep(1)
        challenging_dom_elemets.unhighlight_text(raw_with_delete, "delete")
        time.sleep(1)

        raw_with_edit = challenging_dom_elemets.find_selected_row(ChallengingDomElements.table_rows, "Apeirian2")
        challenging_dom_elemets.highlight_text(raw_with_edit, "edit")
        time.sleep(1)
        challenging_dom_elemets.unhighlight_text(raw_with_edit, "edit")
        time.sleep(1)

        definiebas7_raw = challenging_dom_elemets.find_selected_row(ChallengingDomElements.table_rows, self.definiebas7)
        challenging_dom_elemets.highlight_text(definiebas7_raw, self.definiebas7)
        time.sleep(1)
        challenging_dom_elemets.unhighlight_text(definiebas7_raw, self.definiebas7)
        time.sleep(1)

        iuvaret7_raw = challenging_dom_elemets.find_selected_row(ChallengingDomElements.table_rows, self.iuvaret7)
        challenging_dom_elemets.highlight_text(iuvaret7_raw, self.iuvaret7)
        time.sleep(1)
        challenging_dom_elemets.unhighlight_text(iuvaret7_raw, self.iuvaret7)
        time.sleep(1)

        challenging_dom_elemets.click_button(ChallengingDomElements.qux_button)
        time.sleep(1)
