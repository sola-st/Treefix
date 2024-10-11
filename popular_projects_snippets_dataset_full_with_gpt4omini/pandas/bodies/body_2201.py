# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 5917
arr = ["10/02/2014", "11/02/2014", "12/02/2014"]
expected = DatetimeIndex(
    [datetime(2014, 2, 10), datetime(2014, 2, 11), datetime(2014, 2, 12)]
)
idx1 = DatetimeIndex(arr, dayfirst=True)
idx2 = DatetimeIndex(np.array(arr), dayfirst=True)
idx3 = to_datetime(arr, dayfirst=True, cache=cache)
idx4 = to_datetime(np.array(arr), dayfirst=True, cache=cache)
idx5 = DatetimeIndex(Index(arr), dayfirst=True)
idx6 = DatetimeIndex(Series(arr), dayfirst=True)
tm.assert_index_equal(expected, idx1)
tm.assert_index_equal(expected, idx2)
tm.assert_index_equal(expected, idx3)
tm.assert_index_equal(expected, idx4)
tm.assert_index_equal(expected, idx5)
tm.assert_index_equal(expected, idx6)
