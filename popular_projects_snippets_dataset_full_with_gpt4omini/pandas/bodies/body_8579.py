# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
tz = dateutil.tz.tzlocal()
result = DatetimeIndex(["2018", "NaT"], tz=tz)
expected = DatetimeIndex([Timestamp("2018", tz=tz), pd.NaT])
tm.assert_index_equal(result, expected)
