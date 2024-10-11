# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_nonkeyword_arguments.py
assert str(inspect.signature(g)) == "(a, *, b=0, c=0, d=0)"
