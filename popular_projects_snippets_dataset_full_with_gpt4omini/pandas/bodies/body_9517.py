# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_function.py
arr = pd.array(values, dtype="boolean")

res = np.add.reduce(arr)
if arr[-1] is pd.NA:
    expected = pd.NA
else:
    expected = arr._data.sum()
tm.assert_almost_equal(res, expected)
