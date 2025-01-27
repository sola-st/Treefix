# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
expr = "-lhs"

# float
lhs = Series(np.random.randn(5))
expect = -lhs
result = pd.eval(expr, engine=engine, parser=parser)
tm.assert_series_equal(expect, result)

# int
lhs = Series(np.random.randint(5, size=5))
expect = -lhs
result = pd.eval(expr, engine=engine, parser=parser)
tm.assert_series_equal(expect, result)

# bool doesn't work with numexpr but works elsewhere
lhs = Series(np.random.rand(5) > 0.5)
if engine == "numexpr":
    msg = "couldn't find matching opcode for 'neg_bb'"
    with pytest.raises(NotImplementedError, match=msg):
        pd.eval(expr, engine=engine, parser=parser)
else:
    expect = -lhs
    result = pd.eval(expr, engine=engine, parser=parser)
    tm.assert_series_equal(expect, result)
