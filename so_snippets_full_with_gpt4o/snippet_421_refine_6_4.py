import operator # pragma: no cover

some_function = operator.sub # pragma: no cover

def some_function(arg): # pragma: no cover
    parts = arg.split('-') # pragma: no cover
    if len(parts) != 2: # pragma: no cover
        raise ValueError('Input must be in the format of concatenated terms followed by a subtraction.') # pragma: no cover
    result = sum(map(int, parts[0].split('+'))) - int(parts[1]) # pragma: no cover
    return result # pragma: no cover

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

