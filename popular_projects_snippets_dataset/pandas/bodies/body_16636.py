# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# GH #28870

left = pd.DataFrame({"a": [0, 10, 20], "left_val": [1, 2, 3]})
right = pd.DataFrame({"a": [5, 15, 25], "right_val": [1, 2, 3]})
left["a"] = left["a"].astype(any_int_numpy_dtype)
right["a"] = right["a"].astype(any_int_numpy_dtype)

expected = pd.DataFrame(
    {"a": [0, 10, 20], "left_val": [1, 2, 3], "right_val": [np.nan, 1.0, 2.0]}
)
expected["a"] = expected["a"].astype(any_int_numpy_dtype)

result = merge_asof(left, right, on="a", tolerance=10)
tm.assert_frame_equal(result, expected)
