# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py
exit(signal.rfft3d(
    x, fft_length=[x.shape[-3], x.shape[-2], x.shape[-1]]))
