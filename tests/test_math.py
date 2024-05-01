import pytest

@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2


@pytest.mark.math
def test_two_plus_one():
    a = 1
    b = 2
    c = 3
    assert a + b == c


@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert "division by zero" in str(e.value)


products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]


# automate test using parameters
@pytest.mark.parametrize("a, b, product", products)
@pytest.mark.math
def test_multiply_two_positive_ints(a, b, product):
    assert a * b == product
    
