# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/spectral_ops_test.py
"""Test that spectral_ops.stft/inverse_stft match a NumPy implementation."""
signal = np.random.random(signal_length).astype(np_rtype)
self._compare(signal, frame_length, frame_step, fft_length, tol)
