# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH 20854
expected = Timestamp(f"2016-10-30 03:00:00{offset}", tz="Europe/Helsinki")
result = Timestamp(expected).tz_convert("Europe/Helsinki")
assert result == expected
