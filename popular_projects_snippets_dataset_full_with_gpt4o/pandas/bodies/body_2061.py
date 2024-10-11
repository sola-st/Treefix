# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# coercion
# GH 7930
ser = Series([20121231, 20141231, 99991231])
result = to_datetime(ser, format="%Y%m%d", errors="coerce", cache=cache)
expected = Series(["20121231", "20141231", "NaT"], dtype="M8[ns]")
tm.assert_series_equal(result, expected)
