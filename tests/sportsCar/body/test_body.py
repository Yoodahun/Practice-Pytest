from pytest import mark

@mark.body
class BodyTests:

    @mark.ui
    def test_can_navigate_to_body_page(self, chrome_browser):
        # a = chrome_browser
        print(chrome_browser)
        assert True


    def test_bumper(self):
        assert True

    def test_windshielf(self):
        assert True

