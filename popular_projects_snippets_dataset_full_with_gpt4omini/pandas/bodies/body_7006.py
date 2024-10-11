# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_fillna.py
# Nothing to fill, should still get a copy for the Categorical method,
#  but OK to get a view on CategoricalIndex method
ci = CategoricalIndex([0, 1, 1])
result = ci.fillna(0)
assert result is not ci
assert tm.shares_memory(result, ci)

# But at the EA level we always get a copy.
cat = ci._data
result = cat.fillna(0)
assert result._ndarray is not cat._ndarray
assert result._ndarray.base is None
assert not tm.shares_memory(result, cat)
