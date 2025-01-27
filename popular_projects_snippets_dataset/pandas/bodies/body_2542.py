# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#38604
df = DataFrame([[1, 2, 3]], columns=cols)
rhs = DataFrame([[10, 11]], columns=["d", "e"])
msg = "Columns must be same length as key"
with pytest.raises(ValueError, match=msg):
    df["a"] = rhs
