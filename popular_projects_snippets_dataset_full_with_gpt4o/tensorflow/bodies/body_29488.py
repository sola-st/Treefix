# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
with self.cached_session():
    indices = constant_op.constant([[3], [1]])
    updates = constant_op.constant([9, 10], dtype=dtypes.float32)
    x = array_ops.ones([4], dtype=dtypes.float32)

    theoretical, numerical = gradient_checker_v2.compute_gradient(
        lambda x: array_ops.tensor_scatter_update(x, indices, updates), [x])
    self.assertAllClose(theoretical, numerical, 5e-4, 5e-4)
    theoretical, numerical = gradient_checker_v2.compute_gradient(
        lambda x: array_ops.tensor_scatter_add(x, indices, updates), [x])
    self.assertAllClose(theoretical, numerical, 5e-4, 5e-4)
    theoretical, numerical = gradient_checker_v2.compute_gradient(
        lambda x: array_ops.tensor_scatter_sub(x, indices, updates), [x])
    self.assertAllClose(theoretical, numerical, 5e-4, 5e-4)

    theoretical, numerical = gradient_checker_v2.compute_gradient(
        lambda updates: array_ops.tensor_scatter_update(x, indices, updates),
        [updates])
    self.assertAllClose(theoretical, numerical, 5e-4, 5e-4)
    theoretical, numerical = gradient_checker_v2.compute_gradient(
        lambda updates: array_ops.tensor_scatter_add(x, indices, updates),
        [updates])
    self.assertAllClose(theoretical, numerical, 5e-4, 5e-4)
    theoretical, numerical = gradient_checker_v2.compute_gradient(
        lambda updates: array_ops.tensor_scatter_sub(x, indices, updates),
        [updates])
    self.assertAllClose(theoretical, numerical, 5e-4, 5e-4)
