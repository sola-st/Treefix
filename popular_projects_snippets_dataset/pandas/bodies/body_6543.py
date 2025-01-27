# Extracted from ./data/repos/pandas/pandas/tests/test_take.py
dtype, fill_value, out_dtype = dtype_fill_out_dtype
data = np.random.randint(0, 2, (5, 3)).astype(dtype)
indexer = [2, 1, 0, -1]

result = algos.take_nd(data, indexer, axis=0, fill_value=fill_value)
assert (result[[0, 1, 2], :] == data[[2, 1, 0], :]).all()
assert (result[3, :] == fill_value).all()
assert result.dtype == out_dtype

result = algos.take_nd(data, indexer, axis=1, fill_value=fill_value)
assert (result[:, [0, 1, 2]] == data[:, [2, 1, 0]]).all()
assert (result[:, 3] == fill_value).all()
assert result.dtype == out_dtype

indexer = [2, 1, 0, 1]
result = algos.take_nd(data, indexer, axis=0, fill_value=fill_value)
assert (result[[0, 1, 2, 3], :] == data[indexer, :]).all()
assert result.dtype == dtype

result = algos.take_nd(data, indexer, axis=1, fill_value=fill_value)
assert (result[:, [0, 1, 2, 3]] == data[:, indexer]).all()
assert result.dtype == dtype
