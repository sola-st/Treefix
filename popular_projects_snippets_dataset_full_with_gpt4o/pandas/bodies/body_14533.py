# Extracted from ./data/repos/pandas/pandas/tests/io/test_feather.py
# GH#50765
pa = pytest.importorskip("pyarrow")
df = pd.DataFrame(
    {
        "a": pd.Series([1, np.nan, 3], dtype="Int64"),
        "b": pd.Series([1, 2, 3], dtype="Int64"),
        "c": pd.Series([1.5, np.nan, 2.5], dtype="Float64"),
        "d": pd.Series([1.5, 2.0, 2.5], dtype="Float64"),
        "e": [True, False, None],
        "f": [True, False, True],
        "g": ["a", "b", "c"],
        "h": ["a", "b", None],
    }
)

if string_storage == "python":
    string_array = StringArray(np.array(["a", "b", "c"], dtype=np.object_))
    string_array_na = StringArray(np.array(["a", "b", pd.NA], dtype=np.object_))

else:
    string_array = ArrowStringArray(pa.array(["a", "b", "c"]))
    string_array_na = ArrowStringArray(pa.array(["a", "b", None]))

with tm.ensure_clean() as path:
    to_feather(df, path)
    with pd.option_context("mode.string_storage", string_storage):
        with pd.option_context("mode.dtype_backend", dtype_backend):
            result = read_feather(path, use_nullable_dtypes=True)

expected = pd.DataFrame(
    {
        "a": pd.Series([1, np.nan, 3], dtype="Int64"),
        "b": pd.Series([1, 2, 3], dtype="Int64"),
        "c": pd.Series([1.5, np.nan, 2.5], dtype="Float64"),
        "d": pd.Series([1.5, 2.0, 2.5], dtype="Float64"),
        "e": pd.Series([True, False, pd.NA], dtype="boolean"),
        "f": pd.Series([True, False, True], dtype="boolean"),
        "g": string_array,
        "h": string_array_na,
    }
)

if dtype_backend == "pyarrow":

    from pandas.arrays import ArrowExtensionArray

    expected = pd.DataFrame(
        {
            col: ArrowExtensionArray(pa.array(expected[col], from_pandas=True))
            for col in expected.columns
        }
    )

tm.assert_frame_equal(result, expected)
