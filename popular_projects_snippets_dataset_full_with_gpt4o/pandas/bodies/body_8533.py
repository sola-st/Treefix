# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_datetime.py
# GH#48818
ts = Timestamp("2016-03-11", tz="US/Pacific")
dti = date_range(ts, periods=4)

res = dti - dti[0]
expected = pd.TimedeltaIndex(
    [
        pd.Timedelta(days=0),
        pd.Timedelta(days=1),
        pd.Timedelta(days=2),
        pd.Timedelta(days=2, hours=23),
    ]
)
tm.assert_index_equal(res, expected)
assert res.freq == expected.freq
