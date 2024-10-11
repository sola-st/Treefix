# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py
exit(signal.irfft(x, fft_length=[2 * (x.shape[-1] - 1)]))
