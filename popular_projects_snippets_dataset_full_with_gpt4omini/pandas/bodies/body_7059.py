# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py
idx = CategoricalIndex([0, 0, 0], name="foo")
assert idx.is_unique is False
assert idx.has_duplicates is True

idx = CategoricalIndex([0, 1], categories=[2, 3], name="foo")
assert idx.is_unique is False
assert idx.has_duplicates is True

idx = CategoricalIndex([0, 1, 2, 3], categories=[1, 2, 3], name="foo")
assert idx.is_unique is True
assert idx.has_duplicates is False
