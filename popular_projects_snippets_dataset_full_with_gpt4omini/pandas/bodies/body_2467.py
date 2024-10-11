# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#49837
df = DataFrame(
    {
        "date": to_datetime(
            [datetime(2022, 1, 20), datetime(2022, 1, 22)], utc=utc
        ),
        "update": [True, False],
    }
)
expected = df.copy(deep=True)

update_df = df[df["update"]]

df.loc[df["update"], indexer] = update_df["date"]

tm.assert_frame_equal(df, expected)
