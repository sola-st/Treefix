# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH#22609 Verify filtering operations on DataFrames with categorical Series
df = DataFrame(data=[[0, 0], [1, 1]], columns=["a", "b"])
df["b"] = df["b"].astype("category")

result = df.where(df["a"] > 0)
# Explicitly cast to 'float' to avoid implicit cast when setting np.nan
expected = df.copy().astype({"a": "float"})
expected.loc[0, :] = np.nan

tm.assert_equal(result, expected)
