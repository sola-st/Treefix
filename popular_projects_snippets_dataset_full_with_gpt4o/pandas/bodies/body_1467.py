# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 26779
df = DataFrame(
    data={
        "channel": [1, 2, 3],
        "A": ["String 1", np.NaN, "String 2"],
        "B": [
            Timestamp("2019-06-11 11:00:00"),
            pd.NaT,
            Timestamp("2019-06-11 12:00:00"),
        ],
    }
)
df2 = DataFrame(
    data={"A": ["String 3"], "B": [Timestamp("2019-06-11 12:00:00")]}
)
# Change Columns A and B to df2.values wherever Column A is NaN
df.loc[df["A"].isna(), ["A", "B"]] = df2.values
expected = DataFrame(
    data={
        "channel": [1, 2, 3],
        "A": ["String 1", "String 3", "String 2"],
        "B": [
            Timestamp("2019-06-11 11:00:00"),
            Timestamp("2019-06-11 12:00:00"),
            Timestamp("2019-06-11 12:00:00"),
        ],
    }
)
tm.assert_frame_equal(df, expected)
