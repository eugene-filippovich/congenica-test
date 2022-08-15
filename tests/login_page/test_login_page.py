import pytest

from common.string_helper import get_random_string
from front_end import base_page, login_page, smart_slides_page


class TestLoginPagePositive:
    def test_login_positive(self, user_config):
        # base_page.select_login_tab() commented due to selenium waits 10 minutes for page load
        login_page.input_login(user_config.login, user_config.password)
        login_page.click_submit()
        assert smart_slides_page.new_slideshow_element_hint() == 'Click to create a new slideshow', \
            "Element is not presented"


@pytest.mark.parametrize(("user_name", "password"), [('', ''),
                                                     (get_random_string(1), get_random_string(1)),
                                                     (get_random_string(10), get_random_string(10)),
                                                     (get_random_string(255), get_random_string(255)),
                                                     (get_random_string(256), get_random_string(256)),
                                                     (get_random_string(10000), get_random_string(10000))])
class TestLoginPageNegative:
    def test_login_negative(self, user_config, user_name, password):
        # base_page.select_login_tab() #commented due to selenium waits 10 minutes for page load
        login_page.input_login(user_name, password)
        if user_name == '':
            assert login_page.check_submit_button_disabled(), 'Submit button is enabled'
        if user_name:
            assert login_page.check_submit_button_enabled(), 'Submit button is disabled'
            login_page.click_submit()
            assert login_page.check_validation_message_appears(), "No validation message appears"
