# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append.py

# GH 4993
# appending with datetime will incorrectly convert datetime64

df1 = DataFrame(
    index=[1, 2],
    data=[dt.datetime(2013, 1, 1, 0, 0), dt.datetime(2013, 1, 2, 0, 0)],
    columns=["start_time"],
)
df2 = DataFrame(
    index=[4, 5],
    data=[
        [dt.datetime(2013, 1, 3, 0, 0), dt.datetime(2013, 1, 3, 6, 10)],
        [dt.datetime(2013, 1, 4, 0, 0), dt.datetime(2013, 1, 4, 7, 10)],
    ],
    columns=["start_time", "end_time"],
)

expected = concat(
    [
        Series(
            [
                pd.NaT,
                pd.NaT,
                dt.datetime(2013, 1, 3, 6, 10),
                dt.datetime(2013, 1, 4, 7, 10),
            ],
            name="end_time",
        ),
        Series(
            [
                dt.datetime(2013, 1, 1, 0, 0),
                dt.datetime(2013, 1, 2, 0, 0),
                dt.datetime(2013, 1, 3, 0, 0),
                dt.datetime(2013, 1, 4, 0, 0),
            ],
            name="start_time",
        ),
    ],
    axis=1,
    sort=sort,
)
result = df1._append(df2, ignore_index=True, sort=sort)
if sort:
    expected = expected[["end_time", "start_time"]]
else:
    expected = expected[["start_time", "end_time"]]

tm.assert_frame_equal(result, expected)
