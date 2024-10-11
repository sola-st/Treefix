# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/shape_ops_test.py
signal = constant_op.constant([[1, 2], [11, 12]], dtype=dtypes.float32)
frame_length = 4
frame_step = 1

result = shape_ops.frame(signal, frame_length, frame_step,
                         pad_end=True, pad_value=99)
self.assertAllClose([[[1, 2, 99, 99], [2, 99, 99, 99]],
                     [[11, 12, 99, 99], [12, 99, 99, 99]]], result)

result = shape_ops.frame(signal, frame_length, frame_step,
                         pad_end=False)
self.assertEqual((2, 0, 4), result.shape)

frame_step = 2
result = shape_ops.frame(signal, frame_length, frame_step,
                         pad_end=True, pad_value=99)
self.assertAllClose([[[1, 2, 99, 99]], [[11, 12, 99, 99]]], result)

result = shape_ops.frame(signal, frame_length, frame_step,
                         pad_end=False)
self.assertEqual((2, 0, 4), result.shape)
