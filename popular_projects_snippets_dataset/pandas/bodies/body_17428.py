# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py
offset, cases = norm_cases
for dt, expected in cases.items():
    assert offset._apply(dt) == expected
