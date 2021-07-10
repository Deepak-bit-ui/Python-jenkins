import pytest

@pytest.fixture
def numbers():
    a = 1
    b = 2
    c = 3
    return [a, b, c]
@pytest.mark.skip
def test_method1(numbers):
    assert 1 == numbers[0]

@pytest.mark.xfail
def test_method2(numbers):
    assert 22 == numbers[1]

def test_method3(numbers):
    assert 3 == numbers[2]

