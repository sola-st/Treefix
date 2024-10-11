# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#49159
df = DataFrame(
    {"a": [Timestamp("2022-12-29"), Timestamp("2022-12-30")], **col},
)
df.loc[[1], indexer] = df["a"] + pd.Timedelta(days=1)
expected = DataFrame(
    {"a": [Timestamp("2022-12-29"), Timestamp("2022-12-31")], **col},
)
tm.assert_frame_equal(df, expected)
