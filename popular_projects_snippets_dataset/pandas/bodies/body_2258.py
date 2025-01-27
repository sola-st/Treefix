# Extracted from ./data/repos/pandas/pandas/tests/frame/test_ufunc.py
# unary input, binary output
if is_extension_array_dtype(dtype) or isinstance(dtype, dict):
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Extension / mixed with multiple outputs not implemented."
        )
    )

values = np.array([[-1, -1], [1, 1]], dtype="int64")
df = pd.DataFrame(values, columns=["A", "B"], index=["a", "b"]).astype(dtype=dtype)
result_pandas = np.modf(df)
assert isinstance(result_pandas, tuple)
assert len(result_pandas) == 2
expected_numpy = np.modf(values)

for result, b in zip(result_pandas, expected_numpy):
    expected = pd.DataFrame(b, index=df.index, columns=df.columns)
    tm.assert_frame_equal(result, expected)
