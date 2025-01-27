# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_network.py

# more of an integration test due to the not-public contents portion
# can probably mock this though.
for ext, comp in [("", None), (".gz", "gzip"), (".bz2", "bz2")]:
    df = read_csv(
        "s3://pandas-test/tips.csv" + ext,
        compression=comp,
        storage_options=s3so,
    )
    assert isinstance(df, DataFrame)
    assert not df.empty
    tm.assert_frame_equal(df, tips_df)

# Read public file from bucket with not-public contents
df = read_csv("s3://cant_get_it/tips.csv", storage_options=s3so)
assert isinstance(df, DataFrame)
assert not df.empty
tm.assert_frame_equal(df, tips_df)
