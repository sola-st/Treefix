# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
for dtype in [dtypes.int32, dtypes.int64]:
    paddings = np.zeros((0, 2))
    inp = np.asarray(7)
    with self.cached_session():
        tf_val = array_ops.pad(inp, constant_op.constant(paddings, dtype=dtype))
        out = self.evaluate(tf_val)
    self.assertAllEqual(inp, out)
    self.assertShapeEqual(inp, tf_val)
