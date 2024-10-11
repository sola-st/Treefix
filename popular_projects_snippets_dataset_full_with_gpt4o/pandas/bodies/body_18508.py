# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_ccalendar.py
dt = datetime.fromordinal(1 + np.random.randint(365 * 4000))
result = ccalendar.get_day_of_year(dt.year, dt.month, dt.day)

expected = (dt - dt.replace(month=1, day=1)).days + 1
assert result == expected
