# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/spectral_ops_test.py
"""Test that inverse_stft_window_fn has unit gain at each window phase."""
hann_window = window_ops.hann_window(frame_length, dtype=dtypes.float32)
inverse_window_fn = spectral_ops.inverse_stft_window_fn(frame_step)
inverse_window = inverse_window_fn(frame_length, dtype=dtypes.float32)
hann_window, inverse_window = self.evaluate([hann_window, inverse_window])

# Expect unit gain at each phase of the window.
product_window = hann_window * inverse_window
for i in range(frame_step):
    self.assertAllClose(1.0, np.sum(product_window[i::frame_step]))
