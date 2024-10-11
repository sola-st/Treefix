# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
for _ in range(repeat):
    df.to_parquet(path, **write_kwargs)
    with catch_warnings(record=True):
        actual = read_parquet(path, **read_kwargs)

    tm.assert_frame_equal(
        expected,
        actual,
        check_names=check_names,
        check_like=check_like,
        check_dtype=check_dtype,
    )
