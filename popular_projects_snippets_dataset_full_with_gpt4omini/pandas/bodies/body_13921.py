# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# GH 38714
df = tm.makeDataFrame()
with io.BytesIO() as buffer:
    df.to_csv(buffer, compression=compression, chunksize=1)
    buffer.seek(0)
    tm.assert_frame_equal(
        pd.read_csv(buffer, compression=compression, index_col=0), df
    )
    assert not buffer.closed
