# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_compression.py
# Bucket "pandas-test" created in tests/io/conftest.py

df = pd.read_json('{"a": [1, 2, 3], "b": [4, 5, 6]}')

with tm.ensure_clean() as path:
    df.to_json(path, compression=compression)
    with open(path, "rb") as f:
        s3_resource.Bucket("pandas-test").put_object(Key="test-1", Body=f)

roundtripped_df = pd.read_json(
    "s3://pandas-test/test-1", compression=compression, storage_options=s3so
)
tm.assert_frame_equal(df, roundtripped_df)
