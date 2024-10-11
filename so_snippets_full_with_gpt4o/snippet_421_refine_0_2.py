some_function = lambda x: x  # Mock implementation for the purpose of making the snippet executable # pragma: no cover

some_function = lambda x: x # pragma: no cover
# Adjusting the code snippet to use integers instead of strings for the arithmetic operation # pragma: no cover
a = some_function(123 - 4) # pragma: no cover
a = 123 - 4 # pragma: no cover

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

