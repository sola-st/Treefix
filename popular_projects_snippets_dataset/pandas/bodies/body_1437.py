# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# dispatching _can_hold_element to underlying DatetimeArray
tz = tz_naive_fixture

dti = date_range("2016-01-01", periods=3, tz=tz)
ser = Series(dti)

values = ser._values

newval = "2018-01-01"
values._validate_setitem_value(newval)

indexer_sli(ser)[0] = newval

if tz is None:
    # TODO(EA2D): we can make this no-copy in tz-naive case too
    assert ser.dtype == dti.dtype
    assert ser._values._ndarray is values._ndarray
else:
    assert ser._values is values
