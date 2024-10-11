# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
e = "s + t"
msg = "name 's' is not defined"
with pytest.raises(NameError, match=msg):
    pd.eval(e, engine=engine, parser=parser)
