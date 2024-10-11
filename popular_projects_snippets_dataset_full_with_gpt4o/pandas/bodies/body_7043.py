# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_constructors.py
# see GH#22702
cat = CategoricalIndex([], categories=[True, False])
categories = sorted(cat.categories.tolist())
assert categories == [False, True]
