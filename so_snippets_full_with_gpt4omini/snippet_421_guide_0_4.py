import builtins # pragma: no cover

def some_function(x): return x # pragma: no cover
builtins.int = lambda x: 0 if x == '0' else 1 # pragma: no cover
builtins.str = lambda x: '1' if x == 1 else '0' # pragma: no cover

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

