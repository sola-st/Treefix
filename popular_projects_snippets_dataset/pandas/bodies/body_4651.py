# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
assert np.allclose(nanops._ensure_numeric("1"), 1.0)
assert np.allclose(nanops._ensure_numeric("1.1"), 1.1)
assert np.allclose(nanops._ensure_numeric("1+1j"), 1 + 1j)
