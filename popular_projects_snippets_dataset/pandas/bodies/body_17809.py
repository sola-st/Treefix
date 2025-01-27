# Extracted from ./data/repos/pandas/pandas/tests/tseries/holiday/test_holiday.py
# see gh-10217
msg = "Cannot use both offset and observance"
with pytest.raises(NotImplementedError, match=msg):
    Holiday(
        "Cyber Monday",
        month=11,
        day=1,
        offset=[DateOffset(weekday=SA(4))],
        observance=next_monday,
    )
