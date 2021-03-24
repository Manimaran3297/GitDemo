
import pytest
from selenium import webdriver
import time
driver = None
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")  # keyword to call browser


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("browser",)
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="Driver/chromedriver/chromedriver")
        driver.maximize_window()
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="Driver/geckodriver/geckodriver")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
        """
        Extends the Pytest Plugin to take and embed screenshot in html report,whenever test
        :param item:
        """

        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report,'extra',[])

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if(report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::","_") + ".png"
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228p;" '\
                           'onclick="window.open(this.src)" align="right"/></div>' %file_name
                    extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
     try:
        driver.get_screenshot_as_file(name)
     except:
        print("failed")