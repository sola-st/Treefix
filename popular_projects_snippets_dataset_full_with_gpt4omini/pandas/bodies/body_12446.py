# Extracted from ./data/repos/pandas/pandas/tests/io/test_user_agent.py
headers = {
    "User-Agent": "custom",
    "Auth": "other_custom",
}

pytest.importorskip(engine)

true_df = pd.DataFrame({"column_name": ["column_value"]})
msg = (
    "storage_options passed with file object or non-fsspec file path|"
    "storage_options passed with buffer, or non-supported URL"
)
with pytest.raises(ValueError, match=msg):
    true_df.to_parquet("/tmp/junk.parquet", storage_options=headers, engine=engine)
