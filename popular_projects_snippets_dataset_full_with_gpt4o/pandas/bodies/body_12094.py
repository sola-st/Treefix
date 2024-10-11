# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_network.py
for ext in ["", ".gz", ".bz2"]:
    df = read_csv(
        "s3://pandas-test/tips.csv" + ext,
        engine="python",
        compression="infer",
        storage_options=s3so,
    )
    assert isinstance(df, DataFrame)
    assert not df.empty
    tm.assert_frame_equal(df, tips_df)
