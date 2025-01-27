# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_network.py
for ext, comp in [("", None), (".gz", "gzip"), (".bz2", "bz2")]:
    df = read_csv(
        "s3://pandas-test/tips.csv" + ext,
        engine="python",
        nrows=10,
        compression=comp,
        storage_options=s3so,
    )
    assert isinstance(df, DataFrame)
    assert not df.empty
    tm.assert_frame_equal(tips_df.iloc[:10], df)
