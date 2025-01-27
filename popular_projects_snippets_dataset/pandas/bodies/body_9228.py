# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
# https://github.com/pandas-dev/pandas/issues/16603#issuecomment-
# 349290078
a = Categorical(["a"], categories=["a", "b"])
b = Categorical(["b"], categories=["b", "a"])
assert not a.equals(b)
