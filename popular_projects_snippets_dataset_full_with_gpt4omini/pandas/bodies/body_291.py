# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 25823
assert pd.eval("not True") == -2
assert pd.eval("not False") == -1
assert pd.eval("True and not True") == 0
