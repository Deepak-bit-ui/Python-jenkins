import pytest

@pytest.mark.parametrize("x,y,z", [(5, 20, 100), (10, 10, 100)])
def test_method(x, y, z):
    assert x*y == z
