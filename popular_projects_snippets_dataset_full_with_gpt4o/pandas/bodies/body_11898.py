# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_read_fwf.py
# GH#50289

if string_storage == "pyarrow" or dtype_backend == "pyarrow":
    pa = pytest.importorskip("pyarrow")

if string_storage == "python":
    arr = StringArray(np.array(["a", "b"], dtype=np.object_))
    arr_na = StringArray(np.array([pd.NA, "a"], dtype=np.object_))
else:
    arr = ArrowStringArray(pa.array(["a", "b"]))
    arr_na = ArrowStringArray(pa.array([None, "a"]))

data = """a  b    c      d  e     f  g    h  i
1  2.5  True  a
3  4.5  False b  True  6  7.5  a"""
with pd.option_context("mode.string_storage", string_storage):
    with pd.option_context("mode.dtype_backend", dtype_backend):
        result = read_fwf(StringIO(data), use_nullable_dtypes=True)

expected = DataFrame(
    {
        "a": pd.Series([1, 3], dtype="Int64"),
        "b": pd.Series([2.5, 4.5], dtype="Float64"),
        "c": pd.Series([True, False], dtype="boolean"),
        "d": arr,
        "e": pd.Series([pd.NA, True], dtype="boolean"),
        "f": pd.Series([pd.NA, 6], dtype="Int64"),
        "g": pd.Series([pd.NA, 7.5], dtype="Float64"),
        "h": arr_na,
        "i": pd.Series([pd.NA, pd.NA], dtype="Int64"),
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
    expected["i"] = ArrowExtensionArray(pa.array([None, None]))

tm.assert_frame_equal(result, expected)
