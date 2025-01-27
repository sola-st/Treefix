# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
msg = "bad operand type for unary ~: 'float'"
with pytest.raises(TypeError, match=msg):
    pd.eval("~1.0", engine=engine, parser=parser)

assert pd.eval("-1.0", parser=parser, engine=engine) == -1.0
assert pd.eval("+1.0", parser=parser, engine=engine) == +1.0
assert pd.eval("~1", parser=parser, engine=engine) == ~1
assert pd.eval("-1", parser=parser, engine=engine) == -1
assert pd.eval("+1", parser=parser, engine=engine) == +1
assert pd.eval("~True", parser=parser, engine=engine) == ~True
assert pd.eval("~False", parser=parser, engine=engine) == ~False
assert pd.eval("-True", parser=parser, engine=engine) == -True
assert pd.eval("-False", parser=parser, engine=engine) == -False
assert pd.eval("+True", parser=parser, engine=engine) == +True
assert pd.eval("+False", parser=parser, engine=engine) == +False
