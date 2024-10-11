# Extracted from ./data/repos/pandas/pandas/tests/series/test_ufunc.py
# https://github.com/pandas-dev/pandas/issues/27186
ser = pd.Series([1, 2, 3])
obj = np.array([1, 2, 3])

with pytest.raises(NotImplementedError, match=tm.EMPTY_STRING_PATTERN):
    np.subtract.outer(ser, obj)
