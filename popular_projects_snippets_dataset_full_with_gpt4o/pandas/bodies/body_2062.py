# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 30011
# format='%Y%m%d'
# with None
expected = Series([Timestamp("19801222"), Timestamp("20010112"), NaT])
result = Series(to_datetime(input_s, format="%Y%m%d"))
tm.assert_series_equal(result, expected)
