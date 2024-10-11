# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
e = "s +"
with pytest.raises(SyntaxError, match="invalid syntax"):
    pd.eval(e, engine=engine, parser=parser)
