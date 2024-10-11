# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_index.py
df1 = DataFrame({"A": [1]}, index=["x"])
df2 = DataFrame({"A": [1]}, index=["y"])
msg = "levels supported only when keys is not None"
with pytest.raises(ValueError, match=msg):
    concat([df1, df2], levels=levels)
