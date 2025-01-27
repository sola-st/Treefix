# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_ccalendar.py
result = ccalendar.get_iso_calendar(*input_date_tuple)
expected_from_date_isocalendar = date(*input_date_tuple).isocalendar()
assert result == expected_from_date_isocalendar
assert result == expected_iso_tuple
