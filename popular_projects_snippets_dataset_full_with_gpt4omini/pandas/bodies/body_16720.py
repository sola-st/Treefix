# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 17044
df1 = DataFrame({"key": [1.0, 2.0], "v1": [10, 20]}, columns=["key", "v1"])
df2 = DataFrame({"key": [2], "v2": [200]}, columns=["key", "v2"])
result = df1.merge(df2, on="key", how="left")
expected = DataFrame(
    {"key": [1.0, 2.0], "v1": [10, 20], "v2": [np.nan, 200.0]},
    columns=["key", "v1", "v2"],
)
tm.assert_frame_equal(result, expected)
