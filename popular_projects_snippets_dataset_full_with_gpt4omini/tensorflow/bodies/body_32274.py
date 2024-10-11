# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/mfcc_ops_test.py
"""A basic test that the op runs on random input."""
signal = random_ops.random_normal((2, 3, 5), dtype=dtype)
self.evaluate(mfcc_ops.mfccs_from_log_mel_spectrograms(signal))
