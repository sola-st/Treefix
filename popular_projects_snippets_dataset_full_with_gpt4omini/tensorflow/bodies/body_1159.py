# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py
exit(signal.irfft3d(
    x, fft_length=[x.shape[-3], x.shape[-2], 2 * (x.shape[-1] - 1)]))
