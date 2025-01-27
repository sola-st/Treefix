# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
x = 1  # noqa:F841
gbls = globals().copy()
pd.eval("x + 1", engine=engine, parser=parser)
gbls2 = globals().copy()
assert gbls == gbls2
