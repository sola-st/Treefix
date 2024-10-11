# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
arr = np.array([1, None, "foo", -5.1, NaT, np.nan])
expected = np.array([False, True, False, False, True, True])

self._check_behavior(arr, expected)
