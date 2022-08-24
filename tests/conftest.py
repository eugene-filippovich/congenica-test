import pytest

from selenium import webdriver
from selene.support.shared import config as shared_config
from selene.support.shared import browser
from webdriver_manager.chrome import ChromeDriverManager

from data_structures.common_info import Auth

BROWSER_PATH = ChromeDriverManager().install()


@pytest.fixture(scope='session')
def config():
    yield Auth()


@pytest.fixture(scope='class')
def base_url(config):
    yield config.BASE_URL


@pytest.fixture(autouse=True, scope="class")
def browser_fixture(base_url):
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    shared_config.driver = webdriver.Chrome(executable_path=BROWSER_PATH,
                                            options=chrome_options)

    browser.open(base_url)
    browser.driver.set_window_size(width="1920", height="1080")
    yield browser
    browser.driver.quit()
