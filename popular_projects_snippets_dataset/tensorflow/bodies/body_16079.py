# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_op_test.py
# Build random params & indices matrics w/ the expected shapes.
if axis is None:
    axis = batch_dims
params = np.random.randint(100, size=params_shape, dtype=np.int32)
indices = np.random.randint(
    params_shape[axis], size=indices_shape, dtype=np.int32)

# Use array_ops.gather to get the expected value.
expected = array_ops.gather(
    params, indices, axis=axis, batch_dims=batch_dims)

# Build ragged tensors with varying ragged_ranks from params & axis.
params_tensors = [params] + [
    ragged_tensor.RaggedTensor.from_tensor(params, ragged_rank=i)
    for i in range(1, len(params_shape))
]
indices_tensors = [indices] + [
    ragged_tensor.RaggedTensor.from_tensor(indices, ragged_rank=i)
    for i in range(1, len(indices_shape))
]

# For each combination of params & axis tensors, check that
# ragged_gather_ops.gather matches array_ops.gather.
for params_tensor in params_tensors:
    for indices_tensor in indices_tensors:
        actual = ragged_gather_ops.gather(
            params_tensor, indices_tensor, axis=axis, batch_dims=batch_dims)
        if isinstance(actual, ragged_tensor.RaggedTensor):
            actual = actual.to_tensor()
        self.assertAllEqual(
            expected, actual, 'params.ragged_rank=%s, indices.ragged_rank=%s' %
            (getattr(params_tensor, 'ragged_rank',
                     0), getattr(indices_tensor, 'ragged_rank', 0)))
