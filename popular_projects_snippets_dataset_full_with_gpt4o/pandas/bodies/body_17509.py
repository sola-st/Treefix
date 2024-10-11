# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_month.py
offset, cases = case
for base, expected in cases.items():
    assert_offset_equal(offset, base, expected)
