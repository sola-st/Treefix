# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# no setting allowed
ser = Series(date_range("20130101", periods=5, freq="D"), name="xxx")
with pytest.raises(ValueError, match="modifications"):
    ser.dt.hour = 5

# trying to set a copy
msg = "modifications to a property of a datetimelike.+not supported"
with pd.option_context("chained_assignment", "raise"):
    if using_copy_on_write:
        # TODO(CoW) it would be nice to keep a warning/error for this case
        ser.dt.hour[0] = 5
    else:
        with pytest.raises(SettingWithCopyError, match=msg):
            ser.dt.hour[0] = 5
