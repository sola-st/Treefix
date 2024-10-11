# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_partial_slicing.py
# See also: DatetimeIndex test ofm the same name
dti = date_range("2014-01-01", periods=30, freq="30D")
pi = dti.to_period("D")

ser_montonic = Series(np.arange(30), index=pi)

shuffler = list(range(0, 30, 2)) + list(range(1, 31, 2))
ser = ser_montonic[shuffler]
nidx = ser.index

# Manually identified locations of year==2014
indexer_2014 = np.array(
    [0, 1, 2, 3, 4, 5, 6, 15, 16, 17, 18, 19, 20], dtype=np.intp
)
assert (nidx[indexer_2014].year == 2014).all()
assert not (nidx[~indexer_2014].year == 2014).any()

result = nidx.get_loc("2014")
tm.assert_numpy_array_equal(result, indexer_2014)

expected = ser[indexer_2014]
result = ser.loc["2014"]
tm.assert_series_equal(result, expected)

result = ser["2014"]
tm.assert_series_equal(result, expected)

# Manually identified locations where ser.index is within Mat 2015
indexer_may2015 = np.array([23], dtype=np.intp)
assert nidx[23].year == 2015 and nidx[23].month == 5

result = nidx.get_loc("May 2015")
tm.assert_numpy_array_equal(result, indexer_may2015)

expected = ser[indexer_may2015]
result = ser.loc["May 2015"]
tm.assert_series_equal(result, expected)

result = ser["May 2015"]
tm.assert_series_equal(result, expected)
