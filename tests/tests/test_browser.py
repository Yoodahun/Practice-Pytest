from pytest import mark


@mark.browser
def test_browser_can_navigate_to_training_ground(browser):
    browser.get('http://wwww.google.com')
