# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_month.py
# root cause of #456
offset1 = BMonthEnd()
offset2 = BMonthEnd()
assert not offset1 != offset2
