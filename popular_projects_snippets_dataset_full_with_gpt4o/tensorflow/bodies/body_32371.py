# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/spectral_ops_test.py
"""Test inverse_stft_window_fn in special overlap = 3/4 case."""
# Cases in which frame_length is an integer multiple of 4 * frame_step are
# special because they allow exact reproduction of the waveform with a
# squared Hann window (Hann window in both forward and reverse transforms).
# In the case where frame_length = 4 * frame_step, that combination
# produces a constant gain of 1.5, and so the corrected window will be the
# Hann window / 1.5.
hann_window = window_ops.hann_window(frame_length, dtype=dtypes.float32)
inverse_window_fn = spectral_ops.inverse_stft_window_fn(frame_step)
inverse_window = inverse_window_fn(frame_length, dtype=dtypes.float32)
self.assertAllClose(hann_window, inverse_window * 1.5)
