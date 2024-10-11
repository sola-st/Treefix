# Extracted from ./data/repos/pandas/pandas/core/config_init.py
from pandas.core import nanops

nanops.set_use_bottleneck(cf.get_option(key))
