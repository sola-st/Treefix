def some_function(value): # pragma: no cover
    return value # pragma: no cover
def special_subtract(expression): # pragma: no cover
    parts = expression.split('-') # pragma: no cover
    if len(parts) == 2: # pragma: no cover
        return int(parts[0]) - int(parts[1]) # pragma: no cover
a = special_subtract('123-4') # pragma: no cover
a = special_subtract('123-4') # pragma: no cover

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

