# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
arr = np.array([])
expected = np.array([], dtype=bool)

self._check_behavior(arr, expected)
