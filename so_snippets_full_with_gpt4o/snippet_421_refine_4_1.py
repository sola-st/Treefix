from operator import sub # pragma: no cover

some_function = sub # pragma: no cover

def some_function(input_str): # pragma: no cover
    return int(input_str[:3]) - int(input_str[3:]) # pragma: no cover

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

