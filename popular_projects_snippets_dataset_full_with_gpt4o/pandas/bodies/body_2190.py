# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
array = ["2012", "20120101", "20120101 12:01:01"]
expected = [to_datetime(dt_str, cache=cache) for dt_str in array]
result = [Timestamp(date_str) for date_str in array]
tm.assert_almost_equal(result, expected)
