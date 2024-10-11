# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
with np.errstate(invalid="ignore"):
    exit(np.vstack([arr_complex, arr_nan_nanj]))
