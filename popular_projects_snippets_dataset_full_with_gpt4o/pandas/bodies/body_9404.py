# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_dtypes.py
a = pd.array([0, 1, None], dtype="Int64")
with pytest.raises(ValueError, match=dtype):
    a.to_numpy(dtype=dtype)
