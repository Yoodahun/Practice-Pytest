from pytest import mark


@mark.env
@mark.skip(reason="broken QA env by deploy somenumber")
def test_environment_is_qa(app_config):
    assert app_config.base_url == 'https://myqa-env.com'


@mark.env
def test_environment_is_dev(app_config):
    assert app_config.base_url == 'https://mydev-env.com'


@mark.env
@mark.skip(reason="broken Staging env by deploy somenumber")
def test_environment_is_staging(app_config):
    assert app_config.base_url == 'https://mystaging-env.com'

@mark.env
@mark.xfail(reason="Not ready alpha env yet")
def test_environment_is_alpha(app_config):
    assert app_config.base_url == 'https://myalpha-env.com'
    assert True