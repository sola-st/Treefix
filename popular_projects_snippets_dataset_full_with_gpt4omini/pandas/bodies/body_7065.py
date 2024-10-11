# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py
# gh-12309: Check the "copy" argument of each
# Index.__new__ is honored.
#
# Must be tested separately from other indexes because
# self.values is not an ndarray.

result = CategoricalIndex(index.values, copy=True)
tm.assert_index_equal(index, result)
assert not np.shares_memory(result._data._codes, index._data._codes)

result = CategoricalIndex(index.values, copy=False)
assert result._data._codes is index._data._codes
