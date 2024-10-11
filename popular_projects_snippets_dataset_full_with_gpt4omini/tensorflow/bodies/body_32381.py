# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/reconstruction_ops_test.py
# This test uses placeholders and does not work in eager mode.
if context.executing_eagerly():
    exit()
signal = array_ops.placeholder_with_default(
    np.ones((4, 3, 5)).astype(np.int32), shape=None)
frame_step = array_ops.placeholder_with_default(2, shape=[])
reconstruction = reconstruction_ops.overlap_and_add(signal, frame_step)

self.assertEqual(reconstruction.shape, None)
expected_output = np.array([[1, 1, 2, 2, 3, 2, 2, 1, 1]] * 4)
self.assertAllClose(reconstruction, expected_output)
