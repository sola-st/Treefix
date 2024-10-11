# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# Note: the expected output here is probably incorrect.
# See https://github.com/pandas-dev/pandas/issues/17257 for more.
# We include this as a regression test for GH-24897.
left = DataFrame({"a": [1, 2, 3], "key": [0, 1, 1]})
right = DataFrame({"b": [1, 2, 3]})

expected = DataFrame(
    {"a": [1, 2, 3, None], "key": [0, 1, 1, 2], "b": [1, 2, 2, 3]},
    columns=["a", "key", "b"],
    index=[0, 1, 2, np.nan],
)
result = left.merge(right, left_on="key", right_index=True, how="right")
tm.assert_frame_equal(result, expected)
