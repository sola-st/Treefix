# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
"""Confirms setting batch_dims to zero reduces to tf.gather_nd."""
params = constant_op.constant(np.random.uniform(0.0, 1.0, size=(7, 8, 9)))
indices_shapes = []
indices_shapes.append((1,))
indices_shapes.append((3, 1))
indices_shapes.append((3, 3, 1))
indices_shapes.append((2,))
indices_shapes.append((3, 2))
indices_shapes.append((3, 3, 2))
indices_shapes.append((3,))
indices_shapes.append((3, 3))
indices_shapes.append((3, 3, 3))

for indices_shape in indices_shapes:
    with self.subTest(indices_shape=indices_shape):
        indices = np.random.randint(0, 7, size=indices_shape)
        gather_nd_result = gen_array_ops.gather_nd(params, indices)
        batch_gather_nd_result = array_ops.batch_gather_nd(
            params=params, indices=indices, batch_dims=0)
        self.assertAllEqual(gather_nd_result, batch_gather_nd_result)
