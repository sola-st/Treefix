# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_repr.py
# GH10087
a = Series(Categorical([1, 2, 3, 4]))
exp = (
    "0    1\n1    2\n2    3\n3    4\n"
    "dtype: category\nCategories (4, int64): [1, 2, 3, 4]"
)

with option_context("display.width", None):
    assert exp == repr(a)
