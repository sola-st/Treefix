# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_misc.py
# Ensure is_start/end accessors throw ValueError for CustomBusinessDay,
bday_egypt = offsets.CustomBusinessDay(weekmask="Sun Mon Tue Wed Thu")
dti = date_range(datetime(2013, 4, 30), periods=5, freq=bday_egypt)
msg = "Custom business days is not supported by is_month_start"
with pytest.raises(ValueError, match=msg):
    dti.is_month_start
