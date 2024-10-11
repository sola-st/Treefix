# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_hour.py
_offsets, cases = case
for offset in _offsets:
    for dt, (exp_next, exp_prev) in cases.items():
        assert offset._next_opening_time(dt) == exp_next
        assert offset._prev_opening_time(dt) == exp_prev
