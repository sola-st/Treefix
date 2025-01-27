# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# https://github.com/pandas-dev/pandas/issues/10673
ser = Series(date_range("20130101", periods=5, freq="D"))
with pytest.raises(AttributeError, match="You cannot add any new attribute"):
    ser.dt.xlabel = "a"
