# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 47084
msg = "name '_var_s' is not defined"
e = "_var_s * 2"
with pytest.raises(UndefinedVariableError, match=msg):
    pd.eval(e, engine=engine, parser=parser, global_dict={})
