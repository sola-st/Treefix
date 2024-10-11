# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# GH#25851
# ensure that subclassed datetime works for
# Timedelta operations
result = lh + rh
expected = SubDatetime(2000, 1, 1, 1)
assert result == expected
