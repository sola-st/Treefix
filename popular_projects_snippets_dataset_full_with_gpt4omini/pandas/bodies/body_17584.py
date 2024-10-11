# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_hour.py
offset, cases = case
for dt, expected in cases.items():
    assert offset.is_on_offset(dt) == expected
