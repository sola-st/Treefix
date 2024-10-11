# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
with tm.ensure_clean("test.parquet") as path:
    pathlib.Path(path).write_bytes(b"breakit")
    with pytest.raises(Exception, match=""):  # Not important which exception
        read_parquet(path, engine="fastparquet")
    # The next line raises an error on Windows if the file is still open
    pathlib.Path(path).unlink(missing_ok=False)
