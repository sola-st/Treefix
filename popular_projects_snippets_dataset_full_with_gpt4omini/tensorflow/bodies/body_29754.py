# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
with self.cached_session():
    inp = constant_op.constant(7)
    self.assertAllEqual([7], array_ops.expand_dims(inp, 0))
    self.assertAllEqual([7], array_ops.expand_dims(inp, -1))

    inp = constant_op.constant(True)
    self.assertAllEqual([True], array_ops.expand_dims(inp, 0))
    self.assertAllEqual([True], array_ops.expand_dims(inp, -1))
