# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py
exit(signal.irfft2d(x, fft_length=[x.shape[-2], 2 * (x.shape[-1] - 1)]))
