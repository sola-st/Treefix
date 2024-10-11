# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
dtype = dtypes_for_minmax[0]
max_val = dtypes_for_minmax[2]

# GH 15048
base_df = DataFrame({"A": [1, 1, 1, 1, 2, 2, 2, 2], "B": [3, 4, 3, 2, 2, 3, 2, 1]})
expected_maxs = [3, 4, 4, 4, 2, 3, 3, 3]

df = base_df.astype(dtype)

expected = DataFrame({"B": expected_maxs}).astype(dtype)
result = df.groupby("A").cummax()
tm.assert_frame_equal(result, expected)
result = df.groupby("A", group_keys=False).B.apply(lambda x: x.cummax()).to_frame()
tm.assert_frame_equal(result, expected)

# Test w/ max value for dtype
df.loc[[2, 6], "B"] = max_val
expected.loc[[2, 3, 6, 7], "B"] = max_val
result = df.groupby("A").cummax()
tm.assert_frame_equal(result, expected)
expected = (
    df.groupby("A", group_keys=False).B.apply(lambda x: x.cummax()).to_frame()
)
tm.assert_frame_equal(result, expected)

# Test nan in some values
# Explicit cast to float to avoid implicit cast when setting nan
base_df = base_df.astype({"B": "float"})
base_df.loc[[0, 2, 4, 6], "B"] = np.nan
expected = DataFrame({"B": [np.nan, 4, np.nan, 4, np.nan, 3, np.nan, 3]})
result = base_df.groupby("A").cummax()
tm.assert_frame_equal(result, expected)
expected = (
    base_df.groupby("A", group_keys=False).B.apply(lambda x: x.cummax()).to_frame()
)
tm.assert_frame_equal(result, expected)

# GH 15561
df = DataFrame({"a": [1], "b": pd.to_datetime(["2001"])})
expected = Series(pd.to_datetime("2001"), index=[0], name="b")

result = df.groupby("a")["b"].cummax()
tm.assert_series_equal(expected, result)

# GH 15635
df = DataFrame({"a": [1, 2, 1], "b": [2, 1, 1]})
result = df.groupby("a").b.cummax()
expected = Series([2, 1, 2], name="b")
tm.assert_series_equal(result, expected)
