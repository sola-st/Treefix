# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH 12619, GH#24559
tz = tz_naive_fixture

result = 1293858000000000000
expected = DatetimeIndex([result], tz=tz).asi8[0]
assert result == expected
