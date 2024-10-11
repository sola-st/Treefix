cond1 = 'val1' # pragma: no cover
cond2 = 'val2' # pragma: no cover
cond3 = 'val3' # pragma: no cover
cond4 = 'val4' # pragma: no cover
do_something = lambda: print('Action performed') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/181530/styling-multi-line-conditions-in-if-statements
from l3.Runtime import _l_
if (cond1 == 'val1' and cond2 == 'val2' and
    cond3 == 'val3' and cond4 == 'val4'):
        _l_(2539)

        do_something
        _l_(2538)

