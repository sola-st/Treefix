# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_quantile.py
df = DataFrame([["foo", "a"], ["foo", "b"], ["foo", "c"]], columns=["key", "val"])

with pytest.raises(TypeError, match="cannot be performed against 'object' dtypes"):
    df.groupby("key").quantile()
