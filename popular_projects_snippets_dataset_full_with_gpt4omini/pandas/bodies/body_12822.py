# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_readlines.py
with tm.ensure_clean("test.json") as path:
    df = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    df.to_json(path, lines=True, orient="records")
    reader = JsonReader(
        path,
        orient=None,
        typ="frame",
        dtype=True,
        convert_axes=True,
        convert_dates=True,
        keep_default_dates=True,
        precise_float=False,
        date_unit=None,
        encoding=None,
        lines=True,
        chunksize=chunksize,
        compression=None,
        nrows=None,
    )
    with reader:
        reader.read()
    assert (
        reader.handles.handle.closed
    ), f"didn't close stream with chunksize = {chunksize}"
