# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/spectral_ops_test.py
"""Computes the gradient of the STFT with respect to `signal`."""
stft = spectral_ops.stft(signal, frame_length, frame_step, fft_length)
magnitude_stft = math_ops.abs(stft)
loss = math_ops.reduce_sum(magnitude_stft)
exit(gradients_impl.gradients([loss], [signal])[0])
