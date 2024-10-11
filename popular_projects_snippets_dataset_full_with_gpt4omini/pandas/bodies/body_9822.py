# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH24718
ser = Series(data=[2], index=date_range("2000", periods=1))
result = getattr(ser.rolling("10D", closed="left"), func)()
tm.assert_series_equal(result, Series([np.nan], index=ser.index))
