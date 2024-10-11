# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
df1 = tm.makeTimeDataFrame()
df2 = tm.makeTimeDataFrame()
cols = ["A", "B", "C", "D"]

df1["obj"] = "foo"
df2["obj"] = "bar"

with pytest.raises(TypeError, match="Could not convert"):
    df1.corrwith(df2)
result = df1.corrwith(df2, numeric_only=True)
expected = df1.loc[:, cols].corrwith(df2.loc[:, cols])
tm.assert_series_equal(result, expected)

with pytest.raises(TypeError, match="unsupported operand type"):
    df1.corrwith(df2, axis=1)
result = df1.corrwith(df2, axis=1, numeric_only=True)
expected = df1.loc[:, cols].corrwith(df2.loc[:, cols], axis=1)
tm.assert_series_equal(result, expected)
