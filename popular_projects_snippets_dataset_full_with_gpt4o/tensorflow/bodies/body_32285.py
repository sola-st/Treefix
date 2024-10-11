# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/shape_ops_test.py
signal = np.vstack([np.arange(6),
                    np.arange(6) + 10])
frame_length = 3
frame_step = 2

for rank in range(5):
    nd_signal = np.reshape(signal, (1,) * rank + signal.shape)

    # With padding, we pad the last frame with pad_value.
    result = shape_ops.frame(nd_signal, frame_length, frame_step,
                             pad_end=True, pad_value=99)
    expected_inner_frames = np.array([
        [[0, 1, 2], [2, 3, 4], [4, 5, 99]],
        [[10, 11, 12], [12, 13, 14], [14, 15, 99]]])
    expected = np.reshape(
        expected_inner_frames, (1,) * rank + expected_inner_frames.shape)
    self.assertAllEqual(expected, result)

    # Without padding, we drop the last frame.
    expected_inner_frames = np.array([[[0, 1, 2], [2, 3, 4]],
                                      [[10, 11, 12], [12, 13, 14]]])
    expected = np.reshape(
        expected_inner_frames, (1,) * rank + expected_inner_frames.shape)
    result = shape_ops.frame(nd_signal, frame_length, frame_step,
                             pad_end=False)
    self.assertAllEqual(expected, result)
