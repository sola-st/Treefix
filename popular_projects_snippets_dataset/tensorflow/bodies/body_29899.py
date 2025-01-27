# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reshape_op_test.py
with self.cached_session(use_gpu=use_gpu):
    np_ans = x.reshape(y)
    tf_ans = array_ops.reshape(x, y)
    out = self.evaluate(tf_ans)
    self.assertEqual(tf_ans.get_shape(), out.shape)
    self.assertShapeEqual(np_ans, tf_ans)

    # Repeat with an int64 shape tensor.
    y64 = constant_op.constant(y, dtype=dtypes.int64)
    tf_ans = array_ops.reshape(x, y64)
    out = self.evaluate(tf_ans)
    self.assertEqual(tf_ans.get_shape(), out.shape)
    self.assertShapeEqual(np_ans, tf_ans)
