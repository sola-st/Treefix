# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
x = 1
lcls = locals().copy()
pd.eval("x + 1", local_dict=lcls, engine=engine, parser=parser)
lcls2 = locals().copy()
lcls2.pop("lcls")
assert lcls == lcls2
