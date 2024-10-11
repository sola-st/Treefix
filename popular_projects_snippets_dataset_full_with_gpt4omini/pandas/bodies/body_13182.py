# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
buffer = BytesIO()
df_compat.to_parquet(buffer)
df_from_buf = read_parquet(buffer)
tm.assert_frame_equal(df_compat, df_from_buf)
