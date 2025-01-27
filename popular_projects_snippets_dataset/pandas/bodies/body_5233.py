# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
t1 = Timedelta("1 days 02:34:56.789123456")

for freq, msg in [
    ("Y", "<YearEnd: month=12> is a non-fixed frequency"),
    ("M", "<MonthEnd> is a non-fixed frequency"),
    ("foobar", "Invalid frequency: foobar"),
]:
    with pytest.raises(ValueError, match=msg):
        t1.round(freq)
