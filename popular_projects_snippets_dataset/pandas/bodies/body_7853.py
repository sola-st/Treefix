# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_to_timestamp.py
# GH#44100
dti = date_range("2021-10-18", periods=9, freq="B")
pi = dti.to_period()

result = pi[::2].to_timestamp()
expected = dti[::2]
tm.assert_index_equal(result, expected)

result = pi._data[::2].to_timestamp()
expected = dti._data[::2]
# TODO: can we get the freq to round-trip?
tm.assert_datetime_array_equal(result, expected, check_freq=False)

result = pi[::-1].to_timestamp()
expected = dti[::-1]
tm.assert_index_equal(result, expected)

result = pi._data[::-1].to_timestamp()
expected = dti._data[::-1]
tm.assert_datetime_array_equal(result, expected, check_freq=False)

result = pi[::2][::-1].to_timestamp()
expected = dti[::2][::-1]
tm.assert_index_equal(result, expected)

result = pi._data[::2][::-1].to_timestamp()
expected = dti._data[::2][::-1]
tm.assert_datetime_array_equal(result, expected, check_freq=False)
