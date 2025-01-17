import pytest


@pytest.mark.parametrize('n', list(range(90)))
def test_test(n):
    if n % 10 == 0:
        pytest.fail('Test failure')
