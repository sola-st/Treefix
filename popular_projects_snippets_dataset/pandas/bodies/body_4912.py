# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
result = getattr(obj, opname)()
if not isinstance(obj, PeriodIndex):
    expected = getattr(obj.values, opname)()
else:
    expected = Period(ordinal=getattr(obj.asi8, opname)(), freq=obj.freq)

if getattr(obj, "tz", None) is not None:
    # We need to de-localize before comparing to the numpy-produced result
    expected = expected.astype("M8[ns]").astype("int64")
    assert result.value == expected
else:
    assert result == expected
