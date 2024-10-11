import operator # pragma: no cover

some_function = operator.sub # pragma: no cover

def some_function(arg): # pragma: no cover
    # Assuming arg is a string formatted as '1' + '2' + '3', which would be {'123'} # pragma: no cover
    # Here, we will convert that string into an integer and subtract 4 # pragma: no cover
    if isinstance(arg, str): # pragma: no cover
        return int(arg) - 4 # pragma: no cover
    return arg # pragma: no cover

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

