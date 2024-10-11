# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
a, b = 1, 2  # noqa:F841

if parser != "pandas":
    with pytest.raises(SyntaxError, match="The '@' prefix is only"):
        pd.eval(express, engine=engine, parser=parser)
else:
    with pytest.raises(SyntaxError, match="The '@' prefix is not"):
        pd.eval(express, engine=engine, parser=parser)
