# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
# GH 17575
test = DataFrame(
    {
        "time": [
            Timestamp("2016-06-28 09:35:35"),
            pd.NaT,
            Timestamp("2016-06-28 16:46:28"),
        ],
        "data": ["1", "2", "3"],
    }
)

grouper = Grouper(key="time", freq="h")
result = test.groupby(grouper)["data"].nunique()
expected = test[test.time.notnull()].groupby(grouper)["data"].nunique()
expected.index = expected.index._with_freq(None)
tm.assert_series_equal(result, expected)
