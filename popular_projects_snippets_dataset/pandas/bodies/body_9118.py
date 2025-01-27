# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_repr.py
# GH 33676
result = repr(Categorical([1, "2", 3, 4]))
expected = "[1, '2', 3, 4]\nCategories (4, object): [1, 3, 4, '2']"
assert result == expected
