def some_function(x): return str(int(x) + 1) # pragma: no cover
some_function = some_function # pragma: no cover

def some_function(x): return int(x) # pragma: no cover
a = some_function(int('1') + int('2') + int('3') - int('4')) # pragma: no cover
a = str(int('1') + int('2') + int('3') - int('4')) # pragma: no cover

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

