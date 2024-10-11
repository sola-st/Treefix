# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# same categories, same order
# any combination of None/False are equal
# True/True is the only combination with True that are equal
c1 = CategoricalDtype(list("abc"), ordered1)
c2 = CategoricalDtype(list("abc"), ordered2)
result = c1 == c2
expected = bool(ordered1) is bool(ordered2)
assert result is expected

# same categories, different order
# any combination of None/False are equal (order doesn't matter)
# any combination with True are not equal (different order of cats)
c1 = CategoricalDtype(list("abc"), ordered1)
c2 = CategoricalDtype(list("cab"), ordered2)
result = c1 == c2
expected = (bool(ordered1) is False) and (bool(ordered2) is False)
assert result is expected

# different categories
c2 = CategoricalDtype([1, 2, 3], ordered2)
assert c1 != c2

# none categories
c1 = CategoricalDtype(list("abc"), ordered1)
c2 = CategoricalDtype(None, ordered2)
c3 = CategoricalDtype(None, ordered1)
assert c1 != c2
assert c2 != c1
assert c2 == c3
