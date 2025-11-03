import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


@pytest.mark.github
def test_github_open(driver):
    url = 'https://github.com/'
    driver.get(url)
    assert driver.title == 'GitHub · Change is constant. GitHub keeps you ahead. · GitHub'
    assert driver.current_url == url


@pytest.mark.google
def test_google_open(driver):
    url1 = 'https://www.google.com/'
    driver.get(url1)
    assert driver.title == 'Google'
    assert driver.current_url == url1
