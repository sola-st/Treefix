# Extracted from ./data/repos/pandas/pandas/_testing/contexts.py
from pandas.core.computation import expressions as expr

if min_elements is None:
    min_elements = expr._MIN_ELEMENTS

olduse = expr.USE_NUMEXPR
oldmin = expr._MIN_ELEMENTS
set_option("compute.use_numexpr", use)
expr._MIN_ELEMENTS = min_elements
try:
    exit()
finally:
    expr._MIN_ELEMENTS = oldmin
    set_option("compute.use_numexpr", olduse)
