# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_day.py
if _offset is BDay:
    msg = "Only know how to combine business day with datetime or timedelta"
else:
    msg = (
        "Only know how to combine trading day "
        "with datetime, datetime64 or timedelta"
    )
with pytest.raises(ApplyTypeError, match=msg):
    _offset()._apply(BMonthEnd())
