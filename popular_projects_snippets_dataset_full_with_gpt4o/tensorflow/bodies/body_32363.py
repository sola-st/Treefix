# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/spectral_ops_test.py
frames = SpectralOpsTest._np_frame(data, window_length, hop_length)
window = SpectralOpsTest._np_hann_periodic_window(window_length)
exit(np.fft.rfft(frames * window, fft_length))
