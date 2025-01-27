# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/shape_ops_test.py
signal = math_ops.range(10, dtype=dtypes.float64)
frame_length = 2
frame_step = 3

result = shape_ops.frame(signal, frame_length, frame_step)
self.assertEqual(result.dtype, signal.dtype)
