from pytest import fixture
# from selenium import webdriver
from config import Config

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


@fixture(scope='session')
def env(request):
    print(request)
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg
