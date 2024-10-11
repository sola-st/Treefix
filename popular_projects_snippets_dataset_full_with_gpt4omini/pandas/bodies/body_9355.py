# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_array.py
with pytest.raises(ValueError, match="PandasArray must be 1-dimensional"):
    pd.array(data, dtype="int64")
