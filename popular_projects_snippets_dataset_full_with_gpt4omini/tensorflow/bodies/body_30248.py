# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
"""Tests Tensor batch_dims as input works as intended."""
shapes = []
# params_shape, indices_shape, batch_dims
shapes.append(((3, 2, 2, 3, 4), (3, 2, 3, 1), 0),)
shapes.append(((3, 2, 2, 3, 4), (3, 2, 3, 1), 1),)
shapes.append(((3, 2, 2, 3, 4), (3, 2, 3, 1), 2),)

for params_shape, indices_shape, batch_dims in shapes:
    with self.subTest(
        params_shape=params_shape,
        indices_shape=indices_shape,
        batch_dims=batch_dims):
        params = constant_op.constant(
            np.random.uniform(0.0, 1.0, size=(params_shape)))
        indices = np.random.randint(0, 2, size=indices_shape)
        batch_gather_nd_result = array_ops.gather_nd(
            params=params, indices=indices, batch_dims=batch_dims)
        batch_dims_tensor = constant_op.constant([batch_dims])
        batch_gather_nd_tensor_batch_dims_result = array_ops.gather_nd(
            params=params, indices=indices, batch_dims=batch_dims_tensor)

        self.assertAllEqual(batch_gather_nd_tensor_batch_dims_result,
                            batch_gather_nd_result)
