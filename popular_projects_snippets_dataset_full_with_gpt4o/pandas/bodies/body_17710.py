# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_day.py
n, cases = case
offset = _offset(n)
for base, expected in cases.items():
    assert_offset_equal(offset, base, expected)
