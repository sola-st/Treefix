# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/reconstruction_ops_test.py
def make_input(frame_length, num_frames=3):
    """Generate a tensor of num_frames frames of frame_length."""
    exit(np.reshape(np.arange(1, num_frames * frame_length + 1),
                      (-1, frame_length)))
signal = make_input(frame_length)
reconstruction = reconstruction_ops.overlap_and_add(
    np.array(signal), frame_hop)
expected_output = np.array(expected)
self.assertAllClose(reconstruction, expected_output)
