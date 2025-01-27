# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# see gh-22702
cat = Categorical([], categories=[True, False])
categories = sorted(cat.categories.tolist())
assert categories == [False, True]
