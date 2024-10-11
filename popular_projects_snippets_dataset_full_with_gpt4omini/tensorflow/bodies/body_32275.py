# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/mfcc_ops_test.py
"""A test that the op runs when shape and rank are unknown."""
if context.executing_eagerly():
    exit()
signal = array_ops.placeholder_with_default(
    random_ops.random_normal((2, 3, 5)), tensor_shape.TensorShape(None))
self.assertIsNone(signal.shape.ndims)
self.evaluate(mfcc_ops.mfccs_from_log_mel_spectrograms(signal))
