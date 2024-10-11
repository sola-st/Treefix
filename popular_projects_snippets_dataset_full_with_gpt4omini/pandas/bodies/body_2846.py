# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# with different dtype (GH#3386)
df = DataFrame(
    [["a", "a", np.nan, "a"], ["b", "b", np.nan, "b"], ["c", "c", np.nan, "c"]]
)

result = df.fillna({2: "foo"})
expected = DataFrame(
    [["a", "a", "foo", "a"], ["b", "b", "foo", "b"], ["c", "c", "foo", "c"]]
)
tm.assert_frame_equal(result, expected)

return_value = df.fillna({2: "foo"}, inplace=True)
tm.assert_frame_equal(df, expected)
assert return_value is None
