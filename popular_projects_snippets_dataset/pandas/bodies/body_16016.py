# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isin.py
# GH 50234

ser = Series(data)
result = ser.isin(i for i in isin)
expected_result = Series([True, True, False])

tm.assert_series_equal(result, expected_result)
