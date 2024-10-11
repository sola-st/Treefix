# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# GH#35114
# Case where key's total microseconds happens to match iNaT % 1e6 // 1000
tic = time(minute=12, second=43, microsecond=145224)
dti = DatetimeIndex([pd.NaT])

loc = dti.get_loc(tic)
expected = np.array([], dtype=np.intp)
tm.assert_numpy_array_equal(loc, expected)
