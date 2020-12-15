from pytest import mark


@mark.skip
@mark.tv
@mark.parametrize(
    'tv_brand', [
        ('Samsung'),
        ('Sony'),
        ('Vizio')
    ]
)
def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected")


@mark.tv
def test_television_simple_test(test_data):
    print(f"{test_data} is executing")


