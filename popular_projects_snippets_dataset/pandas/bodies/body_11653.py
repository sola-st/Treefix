# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_dtypes_basic.py
# GH#36712
pa = pytest.importorskip("pyarrow")

with pd.option_context("mode.string_storage", string_storage):

    parser = all_parsers

    data = """a,b
a,x
b,
"""
    result = parser.read_csv(StringIO(data), use_nullable_dtypes=True)

    if string_storage == "python":
        expected = DataFrame(
            {
                "a": StringArray(np.array(["a", "b"], dtype=np.object_)),
                "b": StringArray(np.array(["x", pd.NA], dtype=np.object_)),
            }
        )
    else:
        expected = DataFrame(
            {
                "a": ArrowStringArray(pa.array(["a", "b"])),
                "b": ArrowStringArray(pa.array(["x", None])),
            }
        )
    tm.assert_frame_equal(result, expected)
