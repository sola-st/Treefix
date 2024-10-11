# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py

# integer indexes, be careful
ser = Series(np.random.randn(10), index=list(range(0, 20, 2)))
inds = [0, 4, 6]
arr_inds = np.array([0, 4, 6])

cp = ser.copy()
exp = ser.copy()
ser[inds] = 0
ser.loc[inds] = 0
tm.assert_series_equal(cp, exp)

cp = ser.copy()
exp = ser.copy()
ser[arr_inds] = 0
ser.loc[arr_inds] = 0
tm.assert_series_equal(cp, exp)

inds_notfound = [0, 4, 5, 6]
arr_inds_notfound = np.array([0, 4, 5, 6])
msg = r"\[5\] not in index"
with pytest.raises(KeyError, match=msg):
    ser[inds_notfound] = 0
with pytest.raises(Exception, match=msg):
    ser[arr_inds_notfound] = 0
