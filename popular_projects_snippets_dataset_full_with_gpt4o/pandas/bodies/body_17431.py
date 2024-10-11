# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py
offset, cases = nano_case
for base, expected in cases.items():
    assert_offset_equal(offset, base, expected)
