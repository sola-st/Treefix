# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH#34857
arr = np.array([], dtype=object)
if readonly:
    arr.setflags(write=False)
result = to_datetime(arr)
expected = to_datetime([])
tm.assert_index_equal(result, expected)
