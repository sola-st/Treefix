# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
alt = Timestamp(dt64)

assert str(ts) == str(alt)
assert repr(ts) == repr(alt)
