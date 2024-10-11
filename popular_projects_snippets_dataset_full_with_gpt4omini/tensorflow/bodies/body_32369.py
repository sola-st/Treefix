# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/spectral_ops_test.py
# Generate a random white Gaussian signal.
signal = np.random.normal(size=signal_length).astype(np_rtype)

stft = spectral_ops.stft(signal, frame_length, frame_step, fft_length,
                         pad_end=False)
inverse_stft = spectral_ops.inverse_stft(stft, frame_length, frame_step,
                                         fft_length)
inverse_stft_corrected = spectral_ops.inverse_stft(
    stft, frame_length, frame_step, fft_length,
    window_fn=spectral_ops.inverse_stft_window_fn(frame_step))
inverse_stft, inverse_stft_corrected = self.evaluate(
    [inverse_stft, inverse_stft_corrected])

# Truncate signal to the size of inverse stft.
signal = signal[:inverse_stft.shape[0]]

# Ignore the frame_length samples at either edge.
signal = signal[frame_length:-frame_length]
inverse_stft = inverse_stft[frame_length:-frame_length]
inverse_stft_corrected = inverse_stft_corrected[
    frame_length:-frame_length]

# Check that the inverse and original signal are close up to a scale
# factor.
inverse_stft_scaled = inverse_stft / np.mean(np.abs(inverse_stft))
signal_scaled = signal / np.mean(np.abs(signal))
self.assertLess(np.std(inverse_stft_scaled - signal_scaled), threshold)

# Check that the inverse with correction and original signal are close.
self.assertLess(np.std(inverse_stft_corrected - signal),
                corrected_threshold)
