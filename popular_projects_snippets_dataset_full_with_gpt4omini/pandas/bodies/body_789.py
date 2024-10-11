# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
# see gh-13717: no segfaults!
arr = np.empty_like([None])
expected = np.array([True])

self._check_behavior(arr, expected)
