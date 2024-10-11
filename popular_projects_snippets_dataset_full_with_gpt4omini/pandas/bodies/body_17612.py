# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_quarter.py
offset, dt, expected = case
assert_is_on_offset(offset, dt, expected)
