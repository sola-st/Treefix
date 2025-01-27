# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
arr = np.array([1, 3, np.nan, 5], dtype=float)
expected = np.array([False, False, True, False])

self._check_behavior(arr, expected)
