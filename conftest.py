from pytest import fixture
from selenium import webdriver
from config import Config
import json


#
# @fixture(scope='function')
# def chrome_browser():
#     print("setup before session")
#     yield("            I am function fixture!")
#     print("teardown after session")


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        # default="" #default env.
        help="Environment to run tests against"
    )


def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

@fixture(params=load_test_data('data/testData.json'))
def test_data(request):
    data = request.param
    return data


@fixture(scope='session')
def env(request):
    print(request)
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


@fixture(params=[
    webdriver.Chrome,
    webdriver.Firefox,
    webdriver.Edge
])
def browser(request):
    driver = request.param
    drvr = driver()

    yield drvr

    drvr.quit()

