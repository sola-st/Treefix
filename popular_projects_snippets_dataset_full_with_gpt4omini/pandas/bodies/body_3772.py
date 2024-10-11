# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_convert_dtypes.py
# Specific types are tested in tests/series/test_dtypes.py
# Just check that it works for DataFrame here
df = pd.DataFrame(
    {
        "a": pd.Series([1, 2, 3], dtype=np.dtype("int32")),
        "b": pd.Series(["x", "y", "z"], dtype=np.dtype("O")),
    }
)
with pd.option_context("string_storage", string_storage):
    result = df.convert_dtypes(True, True, convert_integer, False)
expected = pd.DataFrame(
    {
        "a": pd.Series([1, 2, 3], dtype=expected),
        "b": pd.Series(["x", "y", "z"], dtype=f"string[{string_storage}]"),
    }
)
tm.assert_frame_equal(result, expected)
