# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
assert ts.min <= ts
assert ts.min._creso == ts._creso
assert ts.min.value == NaT.value + 1
