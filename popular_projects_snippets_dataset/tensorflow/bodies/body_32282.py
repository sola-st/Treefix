# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/shape_ops_test.py
signal = constant_op.constant([], dtype=dtypes.float32)
frame_length = 2
frame_step = 1

result = self.evaluate(shape_ops.frame(
    signal, frame_length, frame_step, pad_end=True, pad_value=99))
self.assertEqual((0, 2), result.shape)

result = self.evaluate(
    shape_ops.frame(signal, frame_length, frame_step, pad_end=False))
self.assertEqual((0, 2), result.shape)
