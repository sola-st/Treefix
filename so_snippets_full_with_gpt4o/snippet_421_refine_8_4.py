some_function = lambda x: int(x) # pragma: no cover

def some_function(x): # pragma: no cover
    values = x.split('-') # pragma: no cover
    result = sum(int(v) for v in values[0].split('+')) - int(values[1]) # pragma: no cover
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

