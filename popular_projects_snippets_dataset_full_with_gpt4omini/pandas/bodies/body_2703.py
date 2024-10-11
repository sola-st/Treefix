# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_select_dtypes.py
# Fix select_dtypes(include='int') for Windows, FYI #36596
df = DataFrame(
    {
        "a": list("abc"),
        "b": list(range(1, 4)),
        "c": np.arange(3, 6, dtype="int32"),
        "d": np.arange(4.0, 7.0, dtype="float64"),
        "e": [True, False, True],
        "f": pd.date_range("now", periods=3).values,
    }
)
exclude = (np.datetime64,)
result = df.select_dtypes(include=include, exclude=exclude)
expected = df[["b", "c", "e"]]
tm.assert_frame_equal(result, expected)
