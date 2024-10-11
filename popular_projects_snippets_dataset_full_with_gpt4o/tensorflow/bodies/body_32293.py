# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
self._compare_forward(x, rank, fft_length, use_placeholder, rtol, atol)
self._compare_backward(x, rank, fft_length, use_placeholder, rtol, atol)
