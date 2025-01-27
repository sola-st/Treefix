# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
"""Tests whether invalid batch_dims raise expected exceptions."""
params = constant_op.constant(
    np.random.uniform(0.0, 1.0, size=(3, 2, 2, 3, 4)))
indices = np.random.randint(0, 2, size=(3, 2, 3))

with self.assertRaises(TypeError):
    array_ops.batch_gather_nd(
        params=params,
        indices=indices,
        batch_dims=constant_op.constant((0, 1)))

with self.assertRaises(ValueError):
    array_ops.batch_gather_nd(params=params, indices=indices, batch_dims=-1)

with self.assertRaises(ValueError):
    array_ops.batch_gather_nd(params=params, indices=indices, batch_dims=4)
