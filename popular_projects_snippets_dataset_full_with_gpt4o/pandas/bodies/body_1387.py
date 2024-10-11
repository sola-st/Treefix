# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
ser = Series(np.random.randn(10), index=list(range(0, 20, 2)))
ser_original = ser.copy()

for i in range(len(ser)):
    result = ser.iloc[i]
    exp = ser[ser.index[i]]
    tm.assert_almost_equal(result, exp)

# pass a slice
result = ser.iloc[slice(1, 3)]
expected = ser.loc[2:4]
tm.assert_series_equal(result, expected)

# test slice is a view
with tm.assert_produces_warning(None):
    # GH#45324 make sure we aren't giving a spurious FutureWarning
    result[:] = 0
if using_copy_on_write:
    tm.assert_series_equal(ser, ser_original)
else:
    assert (ser.iloc[1:3] == 0).all()

# list of integers
result = ser.iloc[[0, 2, 3, 4, 5]]
expected = ser.reindex(ser.index[[0, 2, 3, 4, 5]])
tm.assert_series_equal(result, expected)
