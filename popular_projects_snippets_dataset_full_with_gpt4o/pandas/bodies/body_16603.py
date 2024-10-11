# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py

df1 = pd.DataFrame({"key": [1, 1, 3], "left_val": [1, 2, 3]})
df2 = pd.DataFrame({"key": [1, 2, 2], "right_val": [1, 2, 3]})
result = merge_asof(df1, df2, on="key")
expected = pd.DataFrame(
    {"key": [1, 1, 3], "left_val": [1, 2, 3], "right_val": [1, 1, 3]}
)
tm.assert_frame_equal(result, expected)
