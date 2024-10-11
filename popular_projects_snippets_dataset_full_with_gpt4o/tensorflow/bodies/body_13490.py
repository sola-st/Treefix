# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/quantized_ops_test.py
expected_output = [1, 1, 2, 127, 255, 255]
with self.session(use_gpu=False) as sess:
    x = constant_op.constant(
        [1.0, 1.25, 1.75, 127.0, 255.0, 500.0],
        shape=[6],
        dtype=dtypes.float32)
    x_min = 0.0
    x_max = 255.0
    op = array_ops.quantize(x, x_min, x_max, dtypes.quint8, mode="MIN_FIRST")
    value = self.evaluate(op)
    self.assertArrayNear(expected_output, value.output, 0.1)
