# Extracted from ./data/repos/pandas/pandas/tests/frame/test_ufunc.py
if is_extension_array_dtype(dtype) or isinstance(dtype, dict):
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Extension / mixed with multiple inputs not implemented."
        )
    )
df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]}, index=["a", "b"]).astype(dtype)
df2 = pd.DataFrame({"A": [1, 2], "B": [3, 4]}, index=["a", "c"]).astype(dtype)
result = np.heaviside(df1, df2)
expected = np.heaviside(
    np.array([[1, 3], [3, 4], [np.nan, np.nan]]),
    np.array([[1, 3], [np.nan, np.nan], [3, 4]]),
)
# TODO(FloatArray): this will be Float64Dtype.
expected = pd.DataFrame(expected, index=["a", "b", "c"], columns=["A", "B"])
tm.assert_frame_equal(result, expected)

result = np.heaviside(df1, df2.values)
expected = pd.DataFrame(
    [[1.0, 1.0], [1.0, 1.0]], columns=["A", "B"], index=["a", "b"]
)
tm.assert_frame_equal(result, expected)
