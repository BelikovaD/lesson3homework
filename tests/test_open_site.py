import pytest


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
