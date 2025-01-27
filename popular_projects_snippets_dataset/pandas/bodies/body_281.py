# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
expr = "+lhs"
expect = lhs

result = pd.eval(expr, engine=engine, parser=parser)
tm.assert_series_equal(expect, result)
