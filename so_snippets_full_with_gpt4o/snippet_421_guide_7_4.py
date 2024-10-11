class MockStr: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
    def __add__(self, other): # pragma: no cover
        pass
 # pragma: no cover
    def __sub__(self, other): # pragma: no cover
        return int(self.value) if self.value.isdigit() else ''.join([c for c in self.value if c not in other]) # pragma: no cover
 # pragma: no cover
    def __str__(self): # pragma: no cover
        return self.value # pragma: no cover
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

