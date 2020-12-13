from pytest import mark


@mark.env
def test_environment_is_qa(app_config):
    assert app_config.base_url == 'https://myqa-env.com'


@mark.env
def test_environment_is_dev(app_config):
    assert app_config.base_url == 'https://mydev-env.com'
