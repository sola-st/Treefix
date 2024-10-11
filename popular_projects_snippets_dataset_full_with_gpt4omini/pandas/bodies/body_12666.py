# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH#50750
pa = pytest.importorskip("pyarrow")
df = DataFrame(
    {
        "a": Series([1, np.nan, 3], dtype="Int64"),
        "b": Series([1, 2, 3], dtype="Int64"),
        "c": Series([1.5, np.nan, 2.5], dtype="Float64"),
        "d": Series([1.5, 2.0, 2.5], dtype="Float64"),
        "e": [True, False, None],
        "f": [True, False, True],
        "g": ["a", "b", "c"],
        "h": ["a", "b", None],
    }
)

if string_storage == "python":
    string_array = StringArray(np.array(["a", "b", "c"], dtype=np.object_))
    string_array_na = StringArray(np.array(["a", "b", NA], dtype=np.object_))

else:
    string_array = ArrowStringArray(pa.array(["a", "b", "c"]))
    string_array_na = ArrowStringArray(pa.array(["a", "b", None]))

out = df.to_json(orient=orient)
with pd.option_context("mode.string_storage", string_storage):
    with pd.option_context("mode.dtype_backend", dtype_backend):
        result = read_json(out, use_nullable_dtypes=True, orient=orient)

expected = DataFrame(
    {
        "a": Series([1, np.nan, 3], dtype="Int64"),
        "b": Series([1, 2, 3], dtype="Int64"),
        "c": Series([1.5, np.nan, 2.5], dtype="Float64"),
        "d": Series([1.5, 2.0, 2.5], dtype="Float64"),
        "e": Series([True, False, NA], dtype="boolean"),
        "f": Series([True, False, True], dtype="boolean"),
        "g": string_array,
        "h": string_array_na,
    }
)

if dtype_backend == "pyarrow":

    from pandas.arrays import ArrowExtensionArray

    expected = DataFrame(
        {
            col: ArrowExtensionArray(pa.array(expected[col], from_pandas=True))
            for col in expected.columns
        }
    )

if orient == "values":
    expected.columns = list(range(0, 8))

tm.assert_frame_equal(result, expected)
