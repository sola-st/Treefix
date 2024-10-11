class MockStr: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
    def __add__(self, other): # pragma: no cover
        return MockStr(self.value + other.value) # pragma: no cover
 # pragma: no cover
    def __sub__(self, other): # pragma: no cover
        return int(self.value) - int(other.value) # pragma: no cover
 # pragma: no cover
    def __str__(self): # pragma: no cover
        return self.value # pragma: no cover
 # pragma: no cover
some_function = lambda x: x # pragma: no cover
result = str(MockStr('1') + MockStr('2') + MockStr('3') - MockStr('4')) # pragma: no cover
a = some_function(result) # pragma: no cover

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

