# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# dispatching _can_hold_element to underling DatetimeArray
tz = tz_naive_fixture

if isinstance(key, slice) and indexer_sli is tm.loc:
    key = slice(0, 1)

dti = date_range("2016-01-01", periods=3, tz=tz)
ser = Series(dti)

values = ser._values

newvals = box(["2019-01-01", "2010-01-02"])
values._validate_setitem_value(newvals)

indexer_sli(ser)[key] = newvals

if tz is None:
    # TODO(EA2D): we can make this no-copy in tz-naive case too
    assert ser.dtype == dti.dtype
    assert ser._values._ndarray is values._ndarray
else:
    assert ser._values is values
