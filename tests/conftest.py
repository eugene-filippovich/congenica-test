import pytest
from data_structures.common_info import Auth
from selenium import webdriver
from selene.support.shared import config as shared_config
from selene.support.shared import browser
from webdriver_manager.chrome import ChromeDriverManager

BROWSER_PATH = ChromeDriverManager().install()


@pytest.fixture(scope='session', autouse=True)
def user_config():
    yield Auth()


@pytest.fixture(autouse=True, scope="class")
def browser_fixture(user_config):
    base_url = f"{user_config.BASE_URL}{user_config.APP_URL}"

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    shared_config.driver = webdriver.Chrome(executable_path=BROWSER_PATH,
                                            options=chrome_options)

    browser.open(base_url)
    browser.driver.set_window_size(width="1920", height="1080")
    yield
    browser.driver.quit()
