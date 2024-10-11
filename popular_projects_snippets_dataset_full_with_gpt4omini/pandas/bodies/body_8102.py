# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
left_index = Index(np.random.permutation(15))
right_index = tm.makeDateIndex(10)

with tm.assert_produces_warning(RuntimeWarning):
    result = left_index.join(right_index, how="outer")

# right_index in this case because DatetimeIndex has join precedence
# over int64 Index
with tm.assert_produces_warning(RuntimeWarning):
    expected = right_index.astype(object).union(left_index.astype(object))

tm.assert_index_equal(result, expected)
