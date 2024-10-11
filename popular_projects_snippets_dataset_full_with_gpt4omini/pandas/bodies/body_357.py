# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 47084
x = 1  # noqa: F841
msg = "name 'x' is not defined"
with pytest.raises(UndefinedVariableError, match=msg):
    pd.eval("x + 1", engine=engine, parser=parser, local_dict={})
