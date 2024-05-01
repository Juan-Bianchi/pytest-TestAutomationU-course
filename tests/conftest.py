import pytest
from stuff.accum import Accumulator

@pytest.fixture
def accum(scope='function'): 
    yield Accumulator()
    print("DONE with the test!") # this fixture will resume execution in this line regardless the test passed or not


@pytest.fixture
def accum2():
    return Accumulator()

# Scopes levels
# function (runs for every test)
# session (runs just for the first test and uses the same value)
# class
# module
# package

