# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH37748
# testing insertion, in a Series of size N (here 5), of a listlike object
# of size  0, N-1, N, N+1

arr = array_fn([0] * size)
expected = Series([arr, 0, 0, 0, 0], index=list("abcde"), dtype=object)

ser = Series(0, index=list("abcde"), dtype=object)
ser.loc["a"] = arr
tm.assert_series_equal(ser, expected)

ser = Series(0, index=list("abcde"), dtype=object)
ser.iloc[0] = arr
tm.assert_series_equal(ser, expected)
