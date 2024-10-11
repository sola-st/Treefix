# Extracted from ./data/repos/pandas/pandas/tests/util/test_util.py
arr = tm.rands_array(5, size=10)
assert arr.shape == (10,)
assert len(arr[0]) == 5
