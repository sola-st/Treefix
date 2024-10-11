# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
arr = np.array([""])  # empty but not na
expected = np.array([False])

self._check_behavior(arr, expected)
