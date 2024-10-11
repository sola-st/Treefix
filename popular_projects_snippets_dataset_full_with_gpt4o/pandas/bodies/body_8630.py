# Extracted from ./data/repos/pandas/pandas/tests/test_expressions.py
df = request.getfixturevalue(fixture)
expr._MIN_ELEMENTS = 0
result, expected = self.call_op(df, df, flex, arith)

if arith == "truediv":
    assert all(x.kind == "f" for x in expected.dtypes.values)
tm.assert_equal(expected, result)

for i in range(len(df.columns)):
    result, expected = self.call_op(df.iloc[:, i], df.iloc[:, i], flex, arith)
    if arith == "truediv":
        assert expected.dtype.kind == "f"
    tm.assert_equal(expected, result)
