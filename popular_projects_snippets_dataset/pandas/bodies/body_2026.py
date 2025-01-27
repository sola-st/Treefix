# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# GH#34857
arr = np.array([], dtype=object)
if readonly:
    arr.setflags(write=False)
result = to_timedelta(arr)
expected = to_timedelta([])
tm.assert_index_equal(result, expected)
