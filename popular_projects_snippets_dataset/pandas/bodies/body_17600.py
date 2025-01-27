# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py
def _check_roundtrip(obj):
    unpickled = tm.round_trip_pickle(obj)
    assert unpickled == obj

_check_roundtrip(offset)
_check_roundtrip(offset2)
_check_roundtrip(offset * 2)
