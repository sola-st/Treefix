# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/spectral_ops_test.py
actual_stft = spectral_ops.stft(
    signal, frame_length, frame_step, fft_length, pad_end=False)
signal_ph = array_ops.placeholder_with_default(signal, shape=signal.shape)
actual_stft_from_ph = spectral_ops.stft(
    signal_ph, frame_length, frame_step, fft_length, pad_end=False)

actual_inverse_stft = spectral_ops.inverse_stft(
    actual_stft, frame_length, frame_step, fft_length)

actual_stft, actual_stft_from_ph, actual_inverse_stft = self.evaluate(
    [actual_stft, actual_stft_from_ph, actual_inverse_stft])

actual_stft_ph = array_ops.placeholder_with_default(
    actual_stft, shape=actual_stft.shape)
actual_inverse_stft_from_ph = self.evaluate(
    spectral_ops.inverse_stft(
        actual_stft_ph, frame_length, frame_step, fft_length))

# Confirm that there is no difference in output when shape/rank is fully
# unknown or known.
self.assertAllClose(actual_stft, actual_stft_from_ph)
self.assertAllClose(actual_inverse_stft, actual_inverse_stft_from_ph)

expected_stft = SpectralOpsTest._np_stft(
    signal, fft_length, frame_step, frame_length)
self.assertAllClose(expected_stft, actual_stft, rtol=tol, atol=tol)

expected_inverse_stft = SpectralOpsTest._np_inverse_stft(
    expected_stft, fft_length, frame_step, frame_length)
self.assertAllClose(
    expected_inverse_stft, actual_inverse_stft, rtol=tol, atol=tol)
