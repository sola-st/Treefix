# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
a = 1  # noqa:F841
expr = " * ".join("a" * 33)
expected = 1
res = pd.eval(expr, engine=engine, parser=parser)
assert res == expected
