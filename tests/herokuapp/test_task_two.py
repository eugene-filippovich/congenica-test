import pytest

from front_end import dynamic_load_elements


class TestTaskTwo:
    @pytest.fixture(scope='class')
    def base_url(self):
        yield "http://the-internet.herokuapp.com/dynamic_loading/1"

    def test_dynamic_element(self):
        dynamic_load_elements.click_start_button()
        dynamic_load_elements.wait_loading_complete()
        print(dynamic_load_elements.print_console_text())
