# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# cross-compat with differing reading/writing engines

df = df_cross_compat
with tm.ensure_clean() as path:
    df.to_parquet(path, engine=pa, compression=None)

    result = read_parquet(path, engine=fp)
    tm.assert_frame_equal(result, df)

    result = read_parquet(path, engine=fp, columns=["a", "d"])
    tm.assert_frame_equal(result, df[["a", "d"]])
