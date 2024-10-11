# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# dispatching _can_hold_element to underling TimedeltaArray
if isinstance(key, slice) and indexer_sli is tm.loc:
    key = slice(0, 1)

tdi = timedelta_range("1 Day", periods=3)
ser = Series(tdi)

values = ser._values

newvals = box(["10 Days", "44 hours"])
values._validate_setitem_value(newvals)

indexer_sli(ser)[key] = newvals
assert ser._values._ndarray is values._ndarray
