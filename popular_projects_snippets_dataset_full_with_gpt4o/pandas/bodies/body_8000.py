# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
# GH#32167 Categorical data and dtype=object should return object-dtype
ci = CategoricalIndex(range(5))
result = Index(ci, dtype=object)
assert not isinstance(result, CategoricalIndex)
