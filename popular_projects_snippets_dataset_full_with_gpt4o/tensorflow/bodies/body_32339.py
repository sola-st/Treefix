# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
with self.session():
    freqs = [[0, 1, 2], [3, 4, -4], [-3, -2, -1]]
    shifted = [[-1, -3, -2], [2, 0, 1], [-4, 3, 4]]
    self.assertAllEqual(fft_ops.fftshift(freqs, axes=(0, 1)), shifted)
    self.assertAllEqual(
        fft_ops.fftshift(freqs, axes=0),
        fft_ops.fftshift(freqs, axes=(0,)))
    self.assertAllEqual(fft_ops.ifftshift(shifted, axes=(0, 1)), freqs)
    self.assertAllEqual(
        fft_ops.ifftshift(shifted, axes=0),
        fft_ops.ifftshift(shifted, axes=(0,)))
    self.assertAllEqual(fft_ops.fftshift(freqs), shifted)
    self.assertAllEqual(fft_ops.ifftshift(shifted), freqs)
