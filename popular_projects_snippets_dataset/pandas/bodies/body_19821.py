# Extracted from ./data/repos/pandas/pandas/core/config_init.py
from pandas.core.util import numba_

numba_.set_use_numba(cf.get_option(key))
