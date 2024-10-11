# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# inspired by asv timeseries.ToDatetimeNONISO8601 benchmark
# see GH-26097 for more
ts_string_1 = "March 1, 2018 12:00:00+0400"
ts_string_2 = "March 1, 2018 12:00:00+0500"
arr = [ts_string_1] * 5 + [ts_string_2] * 5
expected = Index([parse(x) for x in arr])
result = to_datetime(arr, cache=cache)
tm.assert_index_equal(result, expected)
