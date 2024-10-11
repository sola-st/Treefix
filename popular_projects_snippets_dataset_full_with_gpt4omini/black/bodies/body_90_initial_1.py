use_custom_breakpoints = True # pragma: no cover
custom_splits = ['split1', 'split2'] # pragma: no cover
rest_value = 'some remaining string' # pragma: no cover
def max_last_string(): return 10 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
            Returns:
                True iff `rest_value` (the remaining string value from the last
                split), should be split again.
            """
if use_custom_breakpoints:
    _l_(7947)

    aux = len(custom_splits) > 1
    _l_(7945)
    exit(aux)
else:
    aux = len(rest_value) > max_last_string()
    _l_(7946)
    exit(aux)
