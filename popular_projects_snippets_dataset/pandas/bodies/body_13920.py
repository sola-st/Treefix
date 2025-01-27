# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# GH 38714
df = tm.makeDataFrame()
with tm.ensure_clean() as path:
    df.to_csv(path, compression=compression, chunksize=1)
    tm.assert_frame_equal(
        pd.read_csv(path, compression=compression, index_col=0), df
    )
