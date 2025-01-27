# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# using column from DataFrame

ser = string_series
mask = ser > ser.median()
omask = mask.astype(object)

# getitem
result = ser[omask]
expected = ser[mask]
tm.assert_series_equal(result, expected)

# setitem
s2 = ser.copy()
cop = ser.copy()
cop[omask] = 5
s2[mask] = 5
tm.assert_series_equal(cop, s2)

# nans raise exception
omask[5:10] = np.nan
msg = "Cannot mask with non-boolean array containing NA / NaN values"
with pytest.raises(ValueError, match=msg):
    ser[omask]
with pytest.raises(ValueError, match=msg):
    ser[omask] = 5
