# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_convert_dtypes.py
pa = pytest.importorskip("pyarrow")
df = pd.DataFrame(
    {
        "a": pd.Series([1, 2, None], dtype="Int32"),
        "b": pd.Series(["x", "y", None], dtype="string[python]"),
        "c": pd.Series([True, False, None], dtype="boolean"),
        "d": pd.Series([None, 100.5, 200], dtype="Float64"),
    }
)
with pd.option_context("mode.dtype_backend", "pyarrow"):
    result = df.convert_dtypes()
expected = pd.DataFrame(
    {
        "a": pd.arrays.ArrowExtensionArray(
            pa.array([1, 2, None], type=pa.int32())
        ),
        "b": pd.arrays.ArrowExtensionArray(pa.array(["x", "y", None])),
        "c": pd.arrays.ArrowExtensionArray(pa.array([True, False, None])),
        "d": pd.arrays.ArrowExtensionArray(pa.array([None, 100.5, 200.0])),
    }
)
tm.assert_frame_equal(result, expected)
