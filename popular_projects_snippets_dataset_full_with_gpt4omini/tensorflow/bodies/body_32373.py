# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/spectral_ops_test.py
"""Test that spectral_ops.stft has a working gradient."""
# TODO(rjryan): Update gradient tests for Eager.
if context.executing_eagerly():
    exit()
with self.session() as sess:
    signal_length = 512

    # An all-zero signal has all zero gradients with respect to the sum of the
    # magnitude STFT.
    empty_signal = array_ops.zeros([signal_length], dtype=dtypes.float32)
    empty_signal_gradient = sess.run(
        self._compute_stft_gradient(empty_signal))
    self.assertTrue((empty_signal_gradient == 0.0).all())

    # A sinusoid will have non-zero components of its gradient with respect to
    # the sum of the magnitude STFT.
    sinusoid = math_ops.sin(
        2 * np.pi * math_ops.linspace(0.0, 1.0, signal_length))
    sinusoid_gradient = self.evaluate(self._compute_stft_gradient(sinusoid))
    self.assertFalse((sinusoid_gradient == 0.0).all())
