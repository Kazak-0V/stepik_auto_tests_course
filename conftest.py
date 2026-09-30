import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
        help="Выбор браузера: chrome или firefox"
    )


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("browser_name")


@pytest.fixture(scope="function")
def browser(browser_name):
    if browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    driver.implicitly_wait(5)
    yield driver
    driver.quit()