def some_function(value): # pragma: no cover
    return value # pragma: no cover
class MockOperator: # pragma: no cover
    def __sub__(self, other): # pragma: no cover
        return 119 # pragma: no cover
mock_operator = MockOperator() # pragma: no cover
a = some_function(mock_operator - '4') # pragma: no cover

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

