# Extracted from ./data/repos/pandas/pandas/tests/test_expressions.py
c = np.empty(df.shape, dtype=np.bool_)
c.fill(cond)
result = expr.where(c, df.values, df.values + 1)
expected = np.where(c, df.values, df.values + 1)
tm.assert_numpy_array_equal(result, expected)
