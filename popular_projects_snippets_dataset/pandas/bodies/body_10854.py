# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_quantile.py
# https://github.com/pandas-dev/pandas/issues/27470
df = DataFrame({"a": [0, 0, 0, 1, 1, 1], "b": range(6)})
g = df.groupby([0, 0, 0, 1, 1, 1])
with pytest.raises(ValueError, match="Got '50.0' instead"):
    g.quantile(50)

with pytest.raises(ValueError, match="Got '-1.0' instead"):
    g.quantile(-1)
