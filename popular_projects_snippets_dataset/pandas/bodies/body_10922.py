# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nunique.py
# GH 13453
test = DataFrame(
    {
        "time": [
            Timestamp("2016-06-28 09:35:35"),
            Timestamp("2016-06-28 16:09:30"),
            Timestamp("2016-06-28 16:46:28"),
        ],
        "data": ["1", "2", "3"],
    }
).set_index("time")
result = test.groupby(pd.Grouper(freq="h"))["data"].nunique()
expected = test.groupby(pd.Grouper(freq="h"))["data"].apply(Series.nunique)
tm.assert_series_equal(result, expected)
