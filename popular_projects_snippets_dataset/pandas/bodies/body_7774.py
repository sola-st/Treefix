# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_equals.py
assert index.equals(index)
assert index.equals(index.astype(object))
assert index.equals(CategoricalIndex(index))
assert index.equals(CategoricalIndex(index.astype(object)))
