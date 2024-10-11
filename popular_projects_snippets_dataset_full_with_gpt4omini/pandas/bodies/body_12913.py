# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_compression.py

with tm.ensure_clean() as path:
    df = pd.read_json('{"a": ["foo", "bar", "baz"], "b": [4, 5, 6]}')
    df.to_json(path, orient="records", lines=True, compression=compression)

    with pd.read_json(
        path, lines=True, chunksize=1, compression=compression
    ) as res:
        roundtripped_df = pd.concat(res)
    tm.assert_frame_equal(df, roundtripped_df)
