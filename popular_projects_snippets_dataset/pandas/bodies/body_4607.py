# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
with np.errstate(invalid="ignore"):
    exit(arr_inf * 1j)
