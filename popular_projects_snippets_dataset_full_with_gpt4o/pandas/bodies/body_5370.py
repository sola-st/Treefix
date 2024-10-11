# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
tzinfo = tzoffset(None, 7200)
expected = Timestamp("3/11/2012 04:00", tz=tzinfo)
result = Timestamp(expected.to_pydatetime())
assert expected == result
