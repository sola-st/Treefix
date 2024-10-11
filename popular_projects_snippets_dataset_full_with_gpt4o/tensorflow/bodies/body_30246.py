# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
"""Compares results with gather_nd called on every element with map_fn."""
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
    with self.subTest(
        params_shape=params_shape,
        indices_shape=indices_shape,
        batch_dims=batch_dims):
        params = constant_op.constant(
            np.random.uniform(0.0, 1.0, size=(params_shape)))
        indices = np.random.randint(0, 2, size=indices_shape)
        batch_gather_nd_result = array_ops.batch_gather_nd(
            params=params, indices=indices, batch_dims=batch_dims)

        if batch_dims > 1:
            params = array_ops.reshape(
                params, shape=[-1] + list(params_shape[batch_dims:]))
            indices = array_ops.reshape(
                indices, shape=[-1] + list(indices_shape[batch_dims:]))

        map_fn_gather_nd_result = map_fn.map_fn(
            fn=self._map_fn_body, elems=(params, indices), dtype=dtypes.float64)

        if batch_dims > 1:
            out_shape = map_fn_gather_nd_result.shape.as_list()
            out_shape = list(params_shape[:batch_dims]) + out_shape[1:]
            map_fn_gather_nd_result = array_ops.reshape(
                map_fn_gather_nd_result, shape=out_shape)

        self.assertAllEqual(map_fn_gather_nd_result, batch_gather_nd_result)
