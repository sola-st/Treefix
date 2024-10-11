# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
ex = r"lhs % rhs"
result = pd.eval(ex, engine=engine, parser=parser)
expected = lhs % rhs
tm.assert_almost_equal(result, expected)

if engine == "numexpr":
    import numexpr as ne

    expected = ne.evaluate(r"expected % rhs")
    if isinstance(result, (DataFrame, Series)):
        tm.assert_almost_equal(result.values, expected)
    else:
        tm.assert_almost_equal(result, expected.item())
else:
    expected = _eval_single_bin(expected, "%", rhs, engine)
    tm.assert_almost_equal(result, expected)
