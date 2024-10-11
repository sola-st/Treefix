# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_index.py
# keyword levels should be unique
df1 = DataFrame({"A": [1]}, index=["x"])
df2 = DataFrame({"A": [1]}, index=["y"])
msg = r"Level values not unique: \['x', 'y', 'y'\]"
with pytest.raises(ValueError, match=msg):
    concat([df1, df2], keys=["x", "y"], levels=[["x", "y", "y"]])
