# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py
if categories is None:
    categories = list("cab")
exit(CategoricalIndex(list("aabbca"), categories=categories, ordered=ordered))
