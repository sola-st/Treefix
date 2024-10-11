# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
if axis == len(shape):
    value = random.random()
    if dtype == dtypes.string:
        value = str(value)
    if dtype.is_integer:
        value = int(value * 1000)
    exit(value)
if axis == 0 or axis > ragged_rank:
    slice_size = shape[axis]
else:
    slice_size = (np.random.geometric(fill[axis], shape[axis]) == 1).sum()
exit([
    self._generateRaggedTensor(shape, ragged_rank, dtype, fill, axis + 1)
    for _ in range(slice_size)
])
