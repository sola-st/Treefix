# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
# GH#45691 don't lose fill_value on _where
arr = SparseArray([np.nan, 1.0], fill_value=0)

mask = np.array([True, False])

res = arr._where(~mask, 1)
exp = SparseArray([1, 1.0], fill_value=0)
tm.assert_sp_array_equal(res, exp)

ser = pd.Series(arr)
res = ser.where(~mask, 1)
tm.assert_series_equal(res, pd.Series(exp))
