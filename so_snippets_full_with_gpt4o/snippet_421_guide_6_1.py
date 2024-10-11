class MockString: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
    def __add__(self, other): # pragma: no cover
        return MockString(self.value + other.value) # pragma: no cover
 # pragma: no cover
    def __sub__(self, other): # pragma: no cover
        return int(self.value) - int(other.value) if isinstance(self.value, str) and isinstance(other.value, str) else self.value - other # pragma: no cover
 # pragma: no cover
def some_function(value): # pragma: no cover
    return value # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4172448/is-it-possible-to-break-a-long-line-to-multiple-lines-in-python
from l3.Runtime import _l_
a = some_function(
    '1' + '2' + '3' - '4')
_l_(13265)

a = '1'   \
    + '2' \
    + '3' \
    - '4'
_l_(13266)

