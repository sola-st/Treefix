# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
assert int((Timestamp(x).value - Timestamp(y).value) / 1e9) == 0
