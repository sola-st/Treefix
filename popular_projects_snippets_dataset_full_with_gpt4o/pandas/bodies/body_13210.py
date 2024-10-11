# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
df = pd.DataFrame({"a": [1, 2]})

with tm.ensure_clean() as path:
    df.to_parquet(path)
    with pytest.raises(ValueError, match="not supported for the fastparquet"):
        read_parquet(path, engine="fastparquet", use_nullable_dtypes=True)
