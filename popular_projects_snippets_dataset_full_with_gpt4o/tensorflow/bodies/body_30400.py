# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
with context.graph_mode(), self.cached_session():
    x = gen_state_ops.variable(shape=[1], dtype=dtypes.float32)
    result = math_ops.cast(x, dtypes.float32)
    self.assertEqual(x.dtype, dtypes.float32_ref)
    self.assertEqual(result.dtype, dtypes.float32)
