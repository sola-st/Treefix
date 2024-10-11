# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_network.py
# Read with a chunksize
chunksize = 5
for ext, comp in [("", None), (".gz", "gzip"), (".bz2", "bz2")]:
    with read_csv(
        "s3://pandas-test/tips.csv" + ext,
        chunksize=chunksize,
        compression=comp,
        storage_options=s3so,
    ) as df_reader:
        assert df_reader.chunksize == chunksize
        for i_chunk in [0, 1, 2]:
            # Read a couple of chunks and make sure we see them
            # properly.
            df = df_reader.get_chunk()
            assert isinstance(df, DataFrame)
            assert not df.empty
            true_df = tips_df.iloc[
                chunksize * i_chunk : chunksize * (i_chunk + 1)
            ]
            tm.assert_frame_equal(true_df, df)
