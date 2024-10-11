# Extracted from ./data/repos/pandas/pandas/tests/io/test_user_agent.py
if parquet_engine is not None:
    pytest.importorskip(parquet_engine)
    if parquet_engine == "fastparquet":
        pytest.importorskip("fsspec")

custom_user_agent = "Super Cool One"
df_true = pd.DataFrame({"header": [custom_user_agent]})

read_method = wait_until_ready(read_method)
if parquet_engine is None:
    df_http = read_method(
        f"http://localhost:{responder}",
        storage_options={"User-Agent": custom_user_agent},
    )
else:
    df_http = read_method(
        f"http://localhost:{responder}",
        storage_options={"User-Agent": custom_user_agent},
        engine=parquet_engine,
    )

tm.assert_frame_equal(df_true, df_http)
