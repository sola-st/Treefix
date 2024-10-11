def some_function(arg): return int(arg) # pragma: no cover

def some_function(x): return int(x) # pragma: no cover
a = some_function('1') + some_function('2') + some_function('3') - some_function('4') # pragma: no cover
a = some_function('1') + some_function('2') + some_function('3') - some_function('4') # pragma: no cover

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

