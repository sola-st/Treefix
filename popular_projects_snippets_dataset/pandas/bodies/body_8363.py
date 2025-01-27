# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_formats.py
dti = DatetimeIndex([datetime(2012, 2, 7), datetime(2012, 2, 7, 23)])

result = dti.format()
expected = ["2012-02-07 00:00:00", "2012-02-07 23:00:00"]
assert len(result) == 2
assert result == expected
