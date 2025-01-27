# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# CategoricalDtype with categories=None is *not* equal to
#  any fully-initialized CategoricalDtype
first = CategoricalDtype(["a", "b"])
second = CategoricalDtype()
third = CategoricalDtype(ordered=True)

assert second == second
assert third == third

assert first != second
assert second != first
assert first != third
assert third != first
assert second == third
assert third == second
