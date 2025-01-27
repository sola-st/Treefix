# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_datetime.py
# GH#48818
dti = date_range("2016-01-01", periods=12, tz=tz_naive_fixture)

res = dti - dti[0]
expected = pd.timedelta_range("0 Days", "11 Days")
tm.assert_index_equal(res, expected)
assert res.freq == expected.freq
