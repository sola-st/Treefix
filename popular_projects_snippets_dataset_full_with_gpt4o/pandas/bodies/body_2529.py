# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# https://github.com/pandas-dev/pandas/issues/34573
expected = DataFrame(
    {
        "a": Series([0, 1, 2], dtype="int64"),
        "b": Series([1, 2, 3], dtype=float),
        "c": Series([1, 2, 3], dtype=float),
        "d": Series([1, 2, 3], dtype="uint32"),
    }
)
df = DataFrame(
    {
        "a": Series([], dtype="int64"),
        "b": Series([], dtype=float),
        "c": Series([], dtype=float),
        "d": Series([], dtype="uint32"),
    }
)
for idx, b in enumerate([1, 2, 3]):
    df.loc[df.shape[0]] = {
        "a": int(idx),
        "b": float(b),
        "c": float(b),
        "d": np.uint32(b),
    }
tm.assert_frame_equal(df, expected)
