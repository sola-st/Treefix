# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_ccalendar.py
expected = dt.isocalendar()
result = ccalendar.get_iso_calendar(dt.year, dt.month, dt.day)
assert result == expected
