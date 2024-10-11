# Extracted from ./data/repos/pandas/pandas/core/config_init.py
from pandas.core.computation import expressions

expressions.set_use_numexpr(cf.get_option(key))
