# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
s = "inf + 1"
expected = np.inf
result = pd.eval(s, engine=engine, parser=parser)
assert result == expected
