# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_to_numpy.py
con = pd.Series if box else pd.array
arr = con([0.0, 1.0, None], dtype="Float64")
with pytest.raises(ValueError, match=dtype):
    arr.to_numpy(dtype=dtype)
