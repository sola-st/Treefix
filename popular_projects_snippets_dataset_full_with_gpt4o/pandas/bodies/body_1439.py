# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# dispatching _can_hold_element to underling TimedeltaArray
tdi = timedelta_range("1 Day", periods=3)
ser = Series(tdi)

values = ser._values
values._validate_setitem_value(scalar)

indexer_sli(ser)[0] = scalar
assert ser._values._ndarray is values._ndarray
