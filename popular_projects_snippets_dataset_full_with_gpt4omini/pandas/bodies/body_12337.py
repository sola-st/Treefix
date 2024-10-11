# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
original = DataFrame(
    {
        "ColumnOk": [
            0.0,
            np.finfo(np.float32).eps,
            np.finfo(np.float32).max / 10.0,
        ],
        "ColumnTooBig": [
            0.0,
            np.finfo(np.float32).eps,
            np.finfo(np.float32).max,
        ],
    }
)
original.index.name = "index"
for col in original:
    original[col] = original[col].astype(np.float32)

with tm.ensure_clean() as path:
    original.to_stata(path)
    reread = read_stata(path)

original["ColumnTooBig"] = original["ColumnTooBig"].astype(np.float64)
expected = original.copy()
expected.index = expected.index.astype(np.int32)
tm.assert_frame_equal(reread.set_index("index"), expected)
