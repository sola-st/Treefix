# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
month_abbr = calendar.month_abbr[4]
val = f"01-{month_abbr}-2011 00:00:01.978"

format = "%d-%b-%Y %H:%M:%S.%f"
result = to_datetime(val, format=format, cache=cache)
exp = datetime.strptime(val, format)
assert result == exp
