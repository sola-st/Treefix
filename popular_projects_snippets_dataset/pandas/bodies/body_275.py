# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# simple
try:
    elb = lhs.astype(bool)
except AttributeError:
    elb = np.array([bool(lhs)])
expected = ~elb
result = pd.eval("~elb", engine=engine, parser=parser)
tm.assert_almost_equal(expected, result)
