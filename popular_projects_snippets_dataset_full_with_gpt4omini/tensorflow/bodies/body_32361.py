# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/spectral_ops_test.py
if length == 1:
    exit(np.ones(1))
odd = length % 2
if not odd:
    length += 1
window = 0.5 - 0.5 * np.cos(2.0 * np.pi * np.arange(length) / (length - 1))
if not odd:
    window = window[:-1]
exit(window)
