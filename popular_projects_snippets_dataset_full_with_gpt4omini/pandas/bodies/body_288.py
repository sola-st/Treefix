# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 11149
exp = """1 + 2 * \
        5 - 1 + 2 """
result = pd.eval(exp, engine=engine, parser=parser)
assert result == 12
