# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
# GH 13664
arr = [Period("2011-01", freq="M"), NaT, Period("2011-03", freq="M")]
tm.assert_index_equal(Index(arr), PeriodIndex(arr))
tm.assert_index_equal(Index(np.array(arr)), PeriodIndex(np.array(arr)))

arr = [np.nan, NaT, Period("2011-03", freq="M")]
tm.assert_index_equal(Index(arr), PeriodIndex(arr))
tm.assert_index_equal(Index(np.array(arr)), PeriodIndex(np.array(arr)))

arr = [Period("2011-01", freq="M"), NaT, Period("2011-03", freq="D")]
tm.assert_index_equal(Index(arr), Index(arr, dtype=object))

tm.assert_index_equal(Index(np.array(arr)), Index(np.array(arr), dtype=object))
