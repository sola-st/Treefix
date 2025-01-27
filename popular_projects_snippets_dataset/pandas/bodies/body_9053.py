# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_indexing.py
# same tests as GH#12631
sparse = SparseArray([np.nan, 0, 1, 0, 4], fill_value=0)
result = sparse.take(np.array([1, 0, -1]))
expected = SparseArray([0, np.nan, 4], fill_value=0)
tm.assert_sp_array_equal(result, expected)

# fill_value
result = sparse.take(np.array([1, 0, -1]), allow_fill=True)
# TODO: actionable?
# XXX: behavior change.
# the old way of filling self.fill_value doesn't follow EA rules.
# It's supposed to be self.dtype.na_value (nan in this case)
expected = SparseArray([0, np.nan, np.nan], fill_value=0)
tm.assert_sp_array_equal(result, expected)

# allow_fill=False
result = sparse.take(np.array([1, 0, -1]), allow_fill=False, fill_value=True)
expected = SparseArray([0, np.nan, 4], fill_value=0)
tm.assert_sp_array_equal(result, expected)

msg = "Invalid value in 'indices'."
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
    sparse.take(np.array([1, 5]), fill_value=True)
