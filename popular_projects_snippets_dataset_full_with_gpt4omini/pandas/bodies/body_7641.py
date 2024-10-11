# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_get_set.py
# avoid specifying internal representation
# as much as possible
assert len(actual) == len(expected)
for act, exp in zip(actual, expected):
    act = np.asarray(act)
    exp = np.asarray(exp)
    tm.assert_numpy_array_equal(act, exp, check_dtype=check_dtype)
