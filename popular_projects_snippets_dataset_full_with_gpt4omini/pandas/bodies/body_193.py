# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# Check if categorical comparisons on apply, GH 21239
df_values = ["asd", None, 12, "asd", "cde", np.NaN]
df = DataFrame({"a": df_values}, dtype="category")

result = df.a.apply(lambda x: x == val)
expected = Series(
    [np.NaN if pd.isnull(x) else x == val for x in df_values], name="a"
)
tm.assert_series_equal(result, expected)
