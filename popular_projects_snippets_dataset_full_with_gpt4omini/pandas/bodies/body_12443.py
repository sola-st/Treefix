# Extracted from ./data/repos/pandas/pandas/tests/io/test_user_agent.py
if parquet_engine is not None:
    pytest.importorskip(parquet_engine)
    if parquet_engine == "fastparquet":
        pytest.importorskip("fsspec")

read_method = wait_until_ready(read_method)
if parquet_engine is None:
    df_http = read_method(f"http://localhost:{responder}")
else:
    df_http = read_method(f"http://localhost:{responder}", engine=parquet_engine)

assert not df_http.empty
