# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
ex = f"lhs {arith1} rhs"
result = pd.eval(ex, engine=engine, parser=parser)
expected = _eval_single_bin(lhs, arith1, rhs, engine)

tm.assert_almost_equal(result, expected)
ex = f"lhs {arith1} rhs {arith1} rhs"
result = pd.eval(ex, engine=engine, parser=parser)
nlhs = _eval_single_bin(lhs, arith1, rhs, engine)
try:
    nlhs, ghs = nlhs.align(rhs)
except (ValueError, TypeError, AttributeError):
    # ValueError: series frame or frame series align
    # TypeError, AttributeError: series or frame with scalar align
    exit()
else:
    if engine == "numexpr":
        import numexpr as ne

        # direct numpy comparison
        expected = ne.evaluate(f"nlhs {arith1} ghs")
        # Update assert statement due to unreliable numerical
        # precision component (GH37328)
        # TODO: update testing code so that assert_almost_equal statement
        #  can be replaced again by the assert_numpy_array_equal statement
        tm.assert_almost_equal(result.values, expected)
    else:
        expected = eval(f"nlhs {arith1} ghs")
        tm.assert_almost_equal(result, expected)
