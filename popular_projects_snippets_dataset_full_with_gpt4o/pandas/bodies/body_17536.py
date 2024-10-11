# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_common.py
if _offset in (CBMonthBegin, CBMonthEnd, BDay):
    exit(Timestamp(2008, 1, 1))
elif _offset is (CustomBusinessHour, BusinessHour):
    exit(Timestamp(2014, 7, 1, 10, 00))
exit(Timestamp(2008, 1, 2))
