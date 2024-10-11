# Extracted from ./data/repos/pandas/pandas/tests/frame/test_logical_ops.py
result = op(df1)
expected = DataFrame(op(df1.values), index=df1.index, columns=df1.columns)
assert result.values.dtype == np.bool_
tm.assert_frame_equal(result, expected)
