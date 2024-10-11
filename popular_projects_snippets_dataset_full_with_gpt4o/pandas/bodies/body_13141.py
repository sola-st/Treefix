# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
"""Verify parquet serializer and deserializer produce the same results.

    Performs a pandas to disk and disk to pandas round trip,
    then compares the 2 resulting DataFrames to verify equality.

    Parameters
    ----------
    df: Dataframe
    engine: str, optional
        'pyarrow' or 'fastparquet'
    path: str, optional
    write_kwargs: dict of str:str, optional
    read_kwargs: dict of str:str, optional
    expected: DataFrame, optional
        Expected deserialization result, otherwise will be equal to `df`
    check_names: list of str, optional
        Closed set of column names to be compared
    check_like: bool, optional
        If True, ignore the order of index & columns.
    repeat: int, optional
        How many times to repeat the test
    """
write_kwargs = write_kwargs or {"compression": None}
read_kwargs = read_kwargs or {}

if expected is None:
    expected = df

if engine:
    write_kwargs["engine"] = engine
    read_kwargs["engine"] = engine

def compare(repeat):
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

if path is None:
    with tm.ensure_clean() as path:
        compare(repeat)
else:
    compare(repeat)
