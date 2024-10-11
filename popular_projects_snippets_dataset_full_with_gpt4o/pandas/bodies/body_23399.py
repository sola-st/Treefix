# Extracted from ./data/repos/pandas/pandas/core/util/numba_.py
global GLOBAL_USE_NUMBA
if enable:
    import_optional_dependency("numba")
GLOBAL_USE_NUMBA = enable
