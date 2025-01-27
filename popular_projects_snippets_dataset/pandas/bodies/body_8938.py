# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_accessor.py
ser = pd.Series([1, 2, 3])
with pytest.raises(AttributeError, match=".sparse"):
    ser.sparse.density
