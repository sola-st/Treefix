# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reshape_op_test.py
with self.cached_session(use_gpu=use_gpu):
    y = array_ops.reshape(x, shape)
    out = self.evaluate(y)
    self.assertEqual(expected, out.shape)

    # Repeat with an int64 shape tensor.
    shape64 = constant_op.constant(shape, dtype=dtypes.int64)
    y = array_ops.reshape(x, shape64)
    out = self.evaluate(y)
    self.assertEqual(expected, out.shape)
