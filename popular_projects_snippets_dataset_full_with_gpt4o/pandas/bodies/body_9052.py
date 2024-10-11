# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_indexing.py
# similar tests as GH 12631
sparse = SparseArray([np.nan, np.nan, 1, np.nan, 4])
result = sparse.take(np.array([1, 0, -1]))
expected = SparseArray([np.nan, np.nan, 4])
tm.assert_sp_array_equal(result, expected)

# TODO: actionable?
# XXX: test change: fill_value=True -> allow_fill=True
result = sparse.take(np.array([1, 0, -1]), allow_fill=True)
expected = SparseArray([np.nan, np.nan, np.nan])
tm.assert_sp_array_equal(result, expected)

# allow_fill=False
result = sparse.take(np.array([1, 0, -1]), allow_fill=False, fill_value=True)
expected = SparseArray([np.nan, np.nan, 4])
tm.assert_sp_array_equal(result, expected)

msg = "Invalid value in 'indices'"
with pytest.raises(ValueError, match=msg):
    sparse.take(np.array([1, 0, -2]), allow_fill=True)

with pytest.raises(ValueError, match=msg):
    sparse.take(np.array([1, 0, -5]), allow_fill=True)

msg = "out of bounds value in 'indices'"
with pytest.raises(IndexError, match=msg):
    sparse.take(np.array([1, -6]))
with pytest.raises(IndexError, match=msg):
    sparse.take(np.array([1, 5]))
with pytest.raises(IndexError, match=msg):
    sparse.take(np.array([1, 5]), allow_fill=True)
