import time

import pytest
from selenium import webdriver
from options import options


@pytest.fixture
def driver():
    url = options['url']
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    yield driver
    driver.close()
