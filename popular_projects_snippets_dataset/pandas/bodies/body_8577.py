# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH 18785
index = date_range(
    Timestamp(2000, 1, 1),
    Timestamp(2005, 1, 1),
    freq="MS",
    tz="Australia/Melbourne",
)
test = pd.DataFrame({"data": range(len(index))}, index=index)
test = test.resample("Y").mean()
result = DatetimeIndex([x.replace(month=6, day=1) for x in test.index])
expected = DatetimeIndex(
    [
        "2000-06-01 00:00:00",
        "2001-06-01 00:00:00",
        "2002-06-01 00:00:00",
        "2003-06-01 00:00:00",
        "2004-06-01 00:00:00",
        "2005-06-01 00:00:00",
    ],
    tz="Australia/Melbourne",
)
tm.assert_index_equal(result, expected)
