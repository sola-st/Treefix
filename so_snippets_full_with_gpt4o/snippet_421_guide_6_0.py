class Mock: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
    def __sub__(self, other): # pragma: no cover
        pass
 # pragma: no cover
    def __str__(self): # pragma: no cover
        return self.value # pragma: no cover
 # pragma: no cover
some_function = Mock('123') - Mock('4') # pragma: no cover

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

