# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/shape_ops_test.py
if context.executing_eagerly():
    exit()
signal = array_ops.zeros((1, 1), dtype=dtypes.int32)
frame_length = 2
frame_step = 1
# Shape inference is able to detect the rank and inner-most dimension
# if frame_length is known at graph definition time.
result = shape_ops.frame(signal, frame_length, frame_step,
                         pad_end=True, pad_value=99)
self.assertEqual([1, 1, 2], result.shape.as_list())

result = shape_ops.frame(signal, frame_length, frame_step,
                         pad_end=False)
self.assertEqual([1, 0, 2], result.shape.as_list())

# If frame_length is not known, rank and (known) outer and inner dimensions
# are inferred.
signal = array_ops.zeros([1, 2, 3, 4], dtype=dtypes.int32)
frame_length = array_ops.placeholder_with_default(
    ops.convert_to_tensor(0, dtypes.int32), shape=[])
frame_step = 1
result = shape_ops.frame(signal, frame_length, frame_step,
                         pad_end=True, pad_value=99, axis=1)
self.assertEqual([1, 2, None, 3, 4], result.shape.as_list())

result = shape_ops.frame(signal, frame_length, frame_step,
                         pad_end=False, axis=1)
self.assertEqual([1, None, None, 3, 4], result.shape.as_list())

# If frame_length and inner-most dimension is known, rank, inner dimensions,
# and known outer dimensions are inferred.
signal = array_ops.placeholder_with_default(
    array_ops.zeros((0, 5, 0, 20, 5, 3), dtype=dtypes.int32),
    shape=[None, 5, None, 20, 5, 3])
frame_length = 4
frame_step = 3
result = shape_ops.frame(signal, frame_length, frame_step,
                         pad_end=True, pad_value=99, axis=3)
self.assertEqual([None, 5, None, 7, 4, 5, 3], result.shape.as_list())

result = shape_ops.frame(signal, frame_length, frame_step,
                         pad_end=False, axis=3)
self.assertEqual([None, 5, None, 6, 4, 5, 3], result.shape.as_list())

# Test that shape inference is consistent with actual returned shapes for
# small values of signal_length, frame_length, frame_step, and pad_end in
# [True, False].
frame_step = 1
for signal_length in range(2):
    signal = [0] * signal_length
    for frame_length in range(2):
        for pad_end in [False, True]:
            op = shape_ops.frame(signal, frame_length, frame_step,
                                 pad_end=pad_end, pad_value=99)
            result = self.evaluate(op)
            self.assertEqual(op.shape.as_list(), list(result.shape))
