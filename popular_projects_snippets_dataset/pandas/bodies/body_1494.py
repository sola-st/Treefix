# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# see gh-28837
df = DataFrame.from_dict(
    {"date": [1485264372711, 1485265925110, 1540215845888, 1540282121025]}
)

df["date_dt"] = to_datetime(df["date"], unit="ms", cache=True)

df.loc[:, "date_dt_cp"] = df.loc[:, "date_dt"]
df.loc[[2, 3], "date_dt_cp"] = df.loc[[2, 3], "date_dt"]

expected = DataFrame(
    [
        [1485264372711, "2017-01-24 13:26:12.711", "2017-01-24 13:26:12.711"],
        [1485265925110, "2017-01-24 13:52:05.110", "2017-01-24 13:52:05.110"],
        [1540215845888, "2018-10-22 13:44:05.888", "2018-10-22 13:44:05.888"],
        [1540282121025, "2018-10-23 08:08:41.025", "2018-10-23 08:08:41.025"],
    ],
    columns=["date", "date_dt", "date_dt_cp"],
)

columns = ["date_dt", "date_dt_cp"]
expected[columns] = expected[columns].apply(to_datetime)

tm.assert_frame_equal(df, expected)
