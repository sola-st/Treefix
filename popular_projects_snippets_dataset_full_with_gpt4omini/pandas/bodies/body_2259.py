# Extracted from ./data/repos/pandas/pandas/tests/frame/test_ufunc.py
# binop ufuncs are dispatched to our dunder methods.
values = np.array([[-1, -1], [1, 1]], dtype="int64")
df = pd.DataFrame(values, columns=["A", "B"], index=["a", "b"]).astype(dtype=dtype)
result = np.add(df, df)
expected = pd.DataFrame(
    np.add(values, values), index=df.index, columns=df.columns
).astype(dtype)
tm.assert_frame_equal(result, expected)
