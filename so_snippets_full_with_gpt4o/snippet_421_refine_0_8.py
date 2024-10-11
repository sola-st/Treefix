some_function = lambda x: x  # Mock implementation for the purpose of making the snippet executable # pragma: no cover

some_function = lambda x: eval(x.replace('-', '+'))  # Mock implementation that avoids TypeError and makes sense of the input # pragma: no cover

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

