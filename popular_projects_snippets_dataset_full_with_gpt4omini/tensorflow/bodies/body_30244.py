# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
"""Tests for various different shape combinations."""
shapes = []
# params_shape, indices_shape, batch_dims
shapes.append(((2, 2, 2), (2, 1), 1),)
shapes.append(((2, 2, 2), (2, 2), 1),)
shapes.append(((2, 2, 2), (2, 3), 0),)
shapes.append(((2, 2, 2), (3,), 0),)
shapes.append(((2, 2, 2), (1,), 0),)
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
    with self.subTest(
        params_shape=params_shape,
        indices_shape=indices_shape,
        batch_dims=batch_dims):
        params = constant_op.constant(1.0, shape=(params_shape))
        indices = constant_op.constant(
            1, shape=(indices_shape), dtype=dtypes.int32)
        out = array_ops.batch_gather_nd(
            params=params, indices=indices, batch_dims=batch_dims)
        ndims_params = len(params_shape) - batch_dims
        ndims_rows = ndims_params - indices_shape[-1]
        expected_out_shape = indices_shape[:-1]
        if ndims_rows > 0:
            expected_out_shape += params_shape[-ndims_rows:]
        self.assertSequenceEqual(out.shape, expected_out_shape)
