# Extracted from ./data/repos/pandas/pandas/tests/generic/test_series.py
ser = Series([True, False, True])
result = ser._get_bool_data()
tm.assert_series_equal(result, ser)
