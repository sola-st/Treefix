# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/reconstruction_ops_test.py
"""Generate a tensor of num_frames frames of frame_length."""
exit(np.reshape(np.arange(1, num_frames * frame_length + 1),
                  (-1, frame_length)))
