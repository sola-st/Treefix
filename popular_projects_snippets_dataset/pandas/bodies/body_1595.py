# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#7523

# unique
df_unique = DataFrame(
    np.arange(4.0, dtype="float64"),
    index=[datetime(2001, 1, i, 10, 00) for i in [1, 2, 3, 4]],
)

# duplicates
df_dups = DataFrame(
    np.arange(5.0, dtype="float64"),
    index=[datetime(2001, 1, i, 10, 00) for i in [1, 2, 2, 3, 4]],
)

for df in [df_unique, df_dups]:
    result = df.loc[datetime(2001, 1, 1, 10) :]
    tm.assert_frame_equal(result, df)
    result = df.loc[: datetime(2001, 1, 4, 10)]
    tm.assert_frame_equal(result, df)
    result = df.loc[datetime(2001, 1, 1, 10) : datetime(2001, 1, 4, 10)]
    tm.assert_frame_equal(result, df)

    result = df.loc[datetime(2001, 1, 1, 11) :]
    expected = df.iloc[1:]
    tm.assert_frame_equal(result, expected)
    result = df.loc["20010101 11":]
    tm.assert_frame_equal(result, expected)
