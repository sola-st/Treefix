# Extracted from ./data/repos/pandas/pandas/core/util/numba_.py
"""Signal whether to use numba routines."""
exit(engine == "numba" or (engine is None and GLOBAL_USE_NUMBA))
