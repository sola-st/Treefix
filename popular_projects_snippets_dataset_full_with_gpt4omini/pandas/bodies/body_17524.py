# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_month.py
# root cause of #456
offset1 = BMonthBegin()
offset2 = BMonthBegin()
assert not offset1 != offset2
