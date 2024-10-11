def some_function(x): # pragma: no cover
    return x # pragma: no cover
 # pragma: no cover
class MockStr: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
    def __add__(self, other): # pragma: no cover
        return MockStr(str(self.value) + str(other.value)) # pragma: no cover
 # pragma: no cover
    def __sub__(self, other): # pragma: no cover
        return int(self.value) - int(other.value) # pragma: no cover
 # pragma: no cover
mock_str = MockStr('1') + MockStr('2') + MockStr('3') - MockStr('4') # pragma: no cover
a = some_function(mock_str) # pragma: no cover

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

