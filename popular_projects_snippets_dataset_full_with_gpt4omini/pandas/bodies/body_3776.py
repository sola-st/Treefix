# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_convert_dtypes.py
pytest.importorskip("pyarrow")
expected = pd.DataFrame([1, 2, 3], dtype="int64[pyarrow]")
with pd.option_context("mode.dtype_backend", "pyarrow"):
    result = expected.convert_dtypes()
tm.assert_frame_equal(result, expected)
