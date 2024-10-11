# Extracted from ./data/repos/pandas/pandas/tests/util/test_util.py
arr = tm.rands_array(7, size=(10, 10))
assert arr.shape == (10, 10)
assert len(arr[1, 1]) == 7
