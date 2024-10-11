# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/reconstruction_ops_test.py
# This test uses tensor names and does not work in eager mode.
if context.executing_eagerly():
    exit()
signal = array_ops.ones([3, 5])
frame_step = 5
reconstruction = reconstruction_ops.overlap_and_add(signal, frame_step)
self.assertEqual(reconstruction.name, "overlap_and_add/fast_path:0")
expected_output = np.ones([15])
self.assertAllClose(reconstruction, expected_output)
