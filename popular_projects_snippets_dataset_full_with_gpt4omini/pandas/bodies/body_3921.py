# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH12815 Test unstacking with object.
data = Series(["a", "b", "c", "a"], dtype="object")
data.index = MultiIndex.from_tuples(
    [("x", "a"), ("x", "b"), ("y", "b"), ("z", "a")]
)

# By default missing values will be NaN
result = data.unstack()
expected = DataFrame(
    {"a": ["a", np.nan, "a"], "b": ["b", "c", np.nan]}, index=list("xyz")
)
tm.assert_frame_equal(result, expected)

# Fill with any value replaces missing values as expected
result = data.unstack(fill_value="d")
expected = DataFrame(
    {"a": ["a", "d", "a"], "b": ["b", "c", "d"]}, index=list("xyz")
)
tm.assert_frame_equal(result, expected)
