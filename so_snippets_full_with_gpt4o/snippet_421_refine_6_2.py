import operator # pragma: no cover

some_function = operator.sub # pragma: no cover

def some_function(arg): # pragma: no cover
    return int(arg[0]) + int(arg[1]) + int(arg[2]) - int(arg[3]) # pragma: no cover

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

