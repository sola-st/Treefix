# Extracted from ./data/repos/pandas/pandas/tests/test_take.py
dtype, fill_value, out_dtype = dtype_fill_out_dtype
data = np.random.randint(0, 2, 4).astype(dtype)
indexer = [2, 1, 0, -1]

result = algos.take_nd(data, indexer, fill_value=fill_value)
assert (result[[0, 1, 2]] == data[[2, 1, 0]]).all()
assert result[3] == fill_value
assert result.dtype == out_dtype

indexer = [2, 1, 0, 1]

result = algos.take_nd(data, indexer, fill_value=fill_value)
assert (result[[0, 1, 2, 3]] == data[indexer]).all()
assert result.dtype == dtype
