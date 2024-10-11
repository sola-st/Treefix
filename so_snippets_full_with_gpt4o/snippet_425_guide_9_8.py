import pytest # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest
from l3.Runtime import _l_
def test_exception():
    _l_(14985)

    with pytest.raises(Exception) as excinfo:
        _l_(14983)

        function_that_raises_exception()   
        _l_(14982)   
    assert str(excinfo.value) == 'some info' 
    _l_(14984) 

