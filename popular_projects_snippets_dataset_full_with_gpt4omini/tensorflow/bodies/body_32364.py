# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/spectral_ops_test.py
frames = np.fft.irfft(stft, fft_length)
# Pad or truncate frames's inner dimension to window_length.
frames = frames[..., :window_length]
frames = np.pad(frames, [[0, 0]] * (frames.ndim - 1) +
                [[0, max(0, window_length - frames.shape[-1])]], "constant")
window = SpectralOpsTest._np_hann_periodic_window(window_length)
exit(SpectralOpsTest._np_overlap_add(frames * window, hop_length))
