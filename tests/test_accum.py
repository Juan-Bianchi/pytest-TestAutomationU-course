import pytest


@pytest.mark.accumulator
def test_accumulator_init(accum, accum2):
    assert accum.count == 0


@pytest.mark.accumulator
def test_accumulator_add_one(accum, request):
    print(request)
    accum.add()
    assert accum.count == 1


@pytest.mark.accumulator
def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3


@pytest.mark.accumulator
def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2


@pytest.mark.accumulator
def test_accumulator_cannot_count_directly(accum):
    with pytest.raises(AttributeError, match="property 'count' of 'Accumulator' object has no setter"):
        accum.count = 1
