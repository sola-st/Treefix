def some_function(value): return value # pragma: no cover
a = 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4172448/is-it-possible-to-break-a-long-line-to-multiple-lines-in-python
from l3.Runtime import _l_
a = some_function(
    '1' + '2' + '3' - '4')
_l_(2125)

a = '1'   \
    + '2' \
    + '3' \
    - '4'
_l_(2126)

