# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
op = comparison_op

result = op(data_for_compare, other)
assert isinstance(result, SparseArray)
assert result.dtype.subtype == np.bool_

if isinstance(other, SparseArray):
    fill_value = op(data_for_compare.fill_value, other.fill_value)
else:
    fill_value = np.all(
        op(np.asarray(data_for_compare.fill_value), np.asarray(other))
    )

    expected = SparseArray(
        op(data_for_compare.to_dense(), np.asarray(other)),
        fill_value=fill_value,
        dtype=np.bool_,
    )
tm.assert_sp_array_equal(result, expected)
