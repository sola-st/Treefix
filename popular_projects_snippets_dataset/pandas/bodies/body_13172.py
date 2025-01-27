# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH 37105

buf_bytes = df_full.to_parquet(engine=pa)
assert isinstance(buf_bytes, bytes)

buf_stream = BytesIO(buf_bytes)
res = read_parquet(buf_stream)

tm.assert_frame_equal(df_full, res)
