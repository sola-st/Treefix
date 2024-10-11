# Extracted from ./data/repos/pandas/pandas/tests/io/test_feather.py

if expected is None:
    expected = df

with tm.ensure_clean() as path:
    to_feather(df, path, **write_kwargs)

    result = read_feather(path, **read_kwargs)
    tm.assert_frame_equal(result, expected)
