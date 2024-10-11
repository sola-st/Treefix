# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_dtypes.py

msg = "cannot safely"
arr = [1.2, 2.3, 3.7]
with pytest.raises(TypeError, match=msg):
    pd.array(arr, dtype=dtype)

with pytest.raises(TypeError, match=msg):
    pd.Series(arr).astype(dtype)

arr = [1.2, 2.3, 3.7, np.nan]
with pytest.raises(TypeError, match=msg):
    pd.array(arr, dtype=dtype)

with pytest.raises(TypeError, match=msg):
    pd.Series(arr).astype(dtype)
