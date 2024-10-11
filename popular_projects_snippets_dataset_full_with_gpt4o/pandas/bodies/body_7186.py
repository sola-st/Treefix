# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
# coerce things
arr = Index([1, 2, 3, 4])
assert isinstance(arr, self._index_cls)

# but not if explicit dtype passed
arr = Index([1, 2, 3, 4], dtype=object)
assert type(arr) is Index
