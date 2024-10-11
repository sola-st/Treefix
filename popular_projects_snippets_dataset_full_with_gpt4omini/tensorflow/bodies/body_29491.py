# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py

# Loop body as a function to avoid go/gpylint-faq#cell-var-from-loop.
def _TestFn(dtype):
    x = array_ops.ones([4], dtype=dtypes.float32)
    indices = constant_op.constant([[1], [2], [3], [3]], dtype=dtype)
    updates = constant_op.constant([2.0, 0.5, 1.0, 1.0], dtype=dtypes.float32)

    theoretical, _ = gradient_checker_v2.compute_gradient(
        lambda x: array_ops.tensor_scatter_max(x, indices, updates), [x])
    # Numerical gradient doesn't work for degenerate values because the
    # derivative is not continuous. The manually entered gradient divides
    # the gradient among all contributing elements at the discontinuity.
    manual = array_ops.reshape(
        array_ops.matrix_diag([1.0, 0.0, 1.0, 0.3333]), (1, 4, 4))
    self.assertAllClose(theoretical, manual, 5e-4, 5e-4)

    theoretical, _ = gradient_checker_v2.compute_gradient(
        lambda x: array_ops.tensor_scatter_min(x, indices, updates), [x])
    manual = array_ops.reshape(
        array_ops.matrix_diag([1.0, 1.0, 0.0, 0.3333]), (1, 4, 4))
    self.assertAllClose(theoretical, manual, 5e-4, 5e-4)

    theoretical, _ = gradient_checker_v2.compute_gradient(
        lambda updates: array_ops.tensor_scatter_max(x, indices, updates),
        [updates])
    manual = constant_op.constant(
        [[[0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0],
          [0.0, 0.0, 0.3333, 0.3333]]],
        dtype=dtypes.float32)
    self.assertAllClose(theoretical, manual, 5e-4, 5e-4)

    theoretical, _ = gradient_checker_v2.compute_gradient(
        lambda updates: array_ops.tensor_scatter_min(x, indices, updates),
        [updates])
    manual = constant_op.constant(
        [[[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0],
          [0.0, 0.0, 0.3333, 0.3333]]],
        dtype=dtypes.float32)
    self.assertAllClose(theoretical, manual, 5e-4, 5e-4)

with self.cached_session():
    for dtype in (dtypes.int32, dtypes.int64):
        _TestFn(dtype)
