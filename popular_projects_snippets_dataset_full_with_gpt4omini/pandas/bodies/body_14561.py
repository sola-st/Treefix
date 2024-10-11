# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
# GH#50502
if string_storage == "pyarrow" or dtype_backend == "pyarrow":
    pa = pytest.importorskip("pyarrow")

if dtype_backend == "pyarrow" and engine == "c":
    pytest.skip(reason="c engine not yet supported")

if string_storage == "python":
    string_array = StringArray(np.array(["x", "y"], dtype=np.object_))
    string_array_na = StringArray(np.array(["x", NA], dtype=np.object_))

else:
    string_array = ArrowStringArray(pa.array(["x", "y"]))
    string_array_na = ArrowStringArray(pa.array(["x", None]))

text = """a,b,c,d,e,f,g,h,i
x,1,4.0,x,2,4.0,,True,False
y,2,5.0,,,,,False,"""
mock_clipboard[request.node.name] = text

with pd.option_context("mode.string_storage", string_storage):
    with pd.option_context("mode.dtype_backend", dtype_backend):
        result = read_clipboard(
            sep=",", use_nullable_dtypes=True, engine=engine
        )

expected = DataFrame(
    {
        "a": string_array,
        "b": Series([1, 2], dtype="Int64"),
        "c": Series([4.0, 5.0], dtype="Float64"),
        "d": string_array_na,
        "e": Series([2, NA], dtype="Int64"),
        "f": Series([4.0, NA], dtype="Float64"),
        "g": Series([NA, NA], dtype="Int64"),
        "h": Series([True, False], dtype="boolean"),
        "i": Series([False, NA], dtype="boolean"),
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
    expected["g"] = ArrowExtensionArray(pa.array([None, None]))

tm.assert_frame_equal(result, expected)
