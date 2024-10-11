class SomeClass: # pragma: no cover
    def some_function(self, x): # pragma: no cover
        if isinstance(x, str) and '+' in x and '-' in x: # pragma: no cover
            parts = x.split('-') # pragma: no cover
            addition = eval(parts[0]) if '+' in parts[0] else parts[0] # pragma: no cover
            subtraction = int(parts[1].strip()) if parts[1].strip().isdigit() else 0 # pragma: no cover
            return eval(addition) - subtraction # pragma: no cover
        raise ValueError('Incorrect input format') # pragma: no cover
 # pragma: no cover
some_function = SomeClass().some_function # pragma: no cover

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

