# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
def _check_roundtrip(obj):
    unpickled = tm.round_trip_pickle(obj)
    assert unpickled == obj

_check_roundtrip(_offset())
_check_roundtrip(_offset(2))
_check_roundtrip(_offset() * 2)
