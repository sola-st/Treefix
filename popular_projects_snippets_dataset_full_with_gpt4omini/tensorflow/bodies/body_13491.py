# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/quantized_ops_test.py
expected_output = [1.0, 2.0, 4.0, 8.0, 16.0, 255.0]
inp = np.array([1, 2, 4, 8, 16, 255]).astype(np.uint8)
with self.session(use_gpu=False) as sess:
    x = constant_op.constant(inp, shape=[6], dtype=dtypes.quint8)
    x_min = 0.0
    x_max = 255.0
    op = array_ops.dequantize(x, x_min, x_max, mode="MIN_FIRST")
    value = self.evaluate(op)
    self.assertArrayNear(expected_output, value, 0.1)
