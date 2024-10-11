# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# Note: this test passes if instead of using pd.array we use
#  np.array([np.nan, 1]).  Other than that, I (@jbrockmendel)
#  have NO IDEA what the expected behavior is.
# TODO(GH#32306): may be relevant to the expected behavior here.

arr = pd.array([pd.NA, 0, 1], dtype=any_numeric_ea_dtype)
if arr.dtype.kind in ["i", "u"]:
    max_val = np.iinfo(arr.dtype.numpy_dtype).max
else:
    max_val = np.finfo(arr.dtype.numpy_dtype).max
# set value s.t. (at least for integer dtypes) arr._values_for_argsort
#  is not an injection
arr[2] = max_val

left = pd.DataFrame(
    {
        "by_col1": arr,
        "by_col2": ["HELLO", "To", "You"],
        "on_col": [2, 4, 6],
        "value": ["a", "c", "e"],
    }
)
right = pd.DataFrame(
    {
        "by_col1": arr,
        "by_col2": ["WORLD", "Wide", "Web"],
        "on_col": [1, 2, 6],
        "value": ["b", "d", "f"],
    }
)

result = merge_asof(left, right, by=["by_col1", "by_col2"], on="on_col")
expected = pd.DataFrame(
    {
        "by_col1": arr,
        "by_col2": ["HELLO", "To", "You"],
        "on_col": [2, 4, 6],
        "value_x": ["a", "c", "e"],
    }
)
expected["value_y"] = np.array([np.nan, np.nan, np.nan], dtype=object)
tm.assert_frame_equal(result, expected)
