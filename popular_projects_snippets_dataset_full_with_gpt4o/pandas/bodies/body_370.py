# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
with pytest.raises(SyntaxError, match="only a single expression is allowed"):
    pd.eval("1 + 1; 2 + 2", engine=engine, parser=parser)
