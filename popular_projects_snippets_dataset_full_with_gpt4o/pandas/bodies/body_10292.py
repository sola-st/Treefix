# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_size.py
# https://github.com/pandas-dev/pandas/issues/34010
ser = Series([1], index=PeriodIndex(["2000"], name="A", freq="D"))
grp = ser.groupby(level="A")
result = grp.size()
tm.assert_series_equal(result, ser)
