# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
res = variables.Variable(
    initial_value=lambda: array_ops.zeros(shape=[], dtype=dtypes.float32),
    dtype=dtypes.float32)
with self.cached_session():
    self.evaluate(res.initializer)
    with self.assertRaisesOpError("Output must be at least 1-D"):
        state_ops.scatter_nd_update(res, [[0]], [0.22]).eval()
