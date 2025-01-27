# Extracted from ./data/repos/pandas/pandas/tests/series/test_ufunc.py
# Test that ufunc(pd.Series) == pd.Series(ufunc)
arr = np.random.randint(0, 10, 10, dtype="int64")
arr[::2] = 0
if sparse:
    arr = SparseArray(arr, dtype=pd.SparseDtype("int64", 0))

index = list(string.ascii_letters[:10])
name = "name"
series = pd.Series(arr, index=index, name=name)

result = ufunc(series)
expected = pd.Series(ufunc(arr), index=index, name=name)
tm.assert_series_equal(result, expected)
