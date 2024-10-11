# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
paddings = np.zeros((0, 2), dtype=np.int32)
inp = np.asarray(7)
with test_util.use_gpu():
    tf_val = array_ops.pad(inp, paddings)
    out = self.evaluate(tf_val)
self.assertAllEqual(inp, out)
self.assertShapeEqual(inp, tf_val)
