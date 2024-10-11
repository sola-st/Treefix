# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# GH 10050
# GH 13303
ts = Timestamp("2014-12-31 23:59:00", tz=tz)
result = getattr(ts, attr)
# that we are int like
assert isinstance(result, int)
assert result == expected
