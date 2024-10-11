# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
fsspec = pytest.importorskip("fsspec")

path = "memory://test/test.csv"
mode = "wb" if binary_mode else "w"
with fsspec.open(path, mode=mode).open() as fsspec_object:
    df1.to_csv(fsspec_object, index=True)
    assert not fsspec_object.closed

mode = mode.replace("w", "r")
with fsspec.open(path, mode=mode) as fsspec_object:
    df2 = read_csv(
        fsspec_object,
        parse_dates=["dt"],
        index_col=0,
    )
    assert not fsspec_object.closed

tm.assert_frame_equal(df1, df2)
