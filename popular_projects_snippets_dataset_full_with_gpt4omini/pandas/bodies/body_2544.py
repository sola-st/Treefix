# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#39403
df = DataFrame([[1, 2, 3]], columns=["a", "b", "b"])
rhs = DataFrame([[10, 11]], columns=["a", "b"])
msg = "Columns must be same length as key"
with pytest.raises(ValueError, match=msg):
    df[["a", "b"]] = rhs
