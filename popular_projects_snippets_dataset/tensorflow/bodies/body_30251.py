# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
"""Tests gather_nd works with None dimensions."""
shapes = []
# params_shape, indices_shape, batch_dims
shapes.append(((2, 2, 2), (2, 1), 1),)
shapes.append(((2, 2, 2), (2, 2), 1),)
shapes.append(((2, 2, 3, 2), (2, 3), 1),)
shapes.append(((2, 2, 3, 2), (2, 2), 1),)
shapes.append(((2, 2, 3, 2), (2, 1), 1),)
shapes.append(((2, 2, 3, 2), (2, 1, 3), 1),)
shapes.append(((2, 2, 3, 2), (2, 2, 2), 1),)
shapes.append(((2, 2, 3, 2), (2, 3, 1), 1),)
shapes.append(((3, 2, 2, 3, 4), (3, 2, 3), 2),)
shapes.append(((3, 2, 2, 3, 4), (3, 2, 2), 2),)
shapes.append(((3, 2, 2, 3, 4), (3, 2, 1), 2),)
shapes.append(((3, 2, 2, 3, 4), (3, 2, 1, 3), 2),)
shapes.append(((3, 2, 2, 3, 4), (3, 2, 2, 2), 2),)
shapes.append(((3, 2, 2, 3, 4), (3, 2, 3, 1), 2),)

for params_shape, indices_shape, batch_dims in shapes:
    params_ph_shape = list(params_shape)
    indices_ph_shape = list(indices_shape)
    for i in range(batch_dims):
        params_ph_shape[i] = None
        indices_ph_shape[i] = None

    @def_function.function
    def func(params, indices):
        exit(array_ops.batch_gather_nd(
            params=params, indices=indices, batch_dims=batch_dims))  # pylint: disable=cell-var-from-loop

    f = func.get_concrete_function(
        tensor_spec.TensorSpec(params_ph_shape, dtypes.float32),
        tensor_spec.TensorSpec(indices_ph_shape, dtypes.int32))

    params_val = np.ones(dtype=np.float32, shape=params_shape)
    indices_val = np.ones(dtype=np.int32, shape=indices_shape)
    res = f(params_val, indices_val)
    row_ndims = len(params_shape) - batch_dims - indices_shape[-1]
    expected_out_shape = indices_shape[:-1]
    if row_ndims > 0:
        expected_out_shape += params_shape[-row_ndims:]

    self.assertSequenceEqual(res.shape, expected_out_shape)
