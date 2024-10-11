some_function = lambda x: int(x) # pragma: no cover

def some_function(val): # pragma: no cover
    # Split the string into its components, convert them to integers, and perform the operations # pragma: no cover
    parts = val.split('-') # pragma: no cover
    total = sum(int(part) for part in parts[0].split('+')) - int(parts[1]) # pragma: no cover
    return total # pragma: no cover

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

