# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
with self.session():
    x = [0, 1, 2, 3, 4, -4, -3, -2, -1]
    y = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    self.assertAllEqual(fft_ops.fftshift(x), np.fft.fftshift(x))
    self.assertAllEqual(fft_ops.ifftshift(y), np.fft.ifftshift(y))
    x = [0, 1, 2, 3, 4, -5, -4, -3, -2, -1]
    y = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
    self.assertAllEqual(fft_ops.fftshift(x), np.fft.fftshift(x))
    self.assertAllEqual(fft_ops.ifftshift(y), np.fft.ifftshift(y))
    freqs = [[0, 1, 2], [3, 4, -4], [-3, -2, -1]]
    shifted = [[-1, -3, -2], [2, 0, 1], [-4, 3, 4]]
    self.assertAllEqual(
        fft_ops.fftshift(freqs, axes=(0, 1)),
        np.fft.fftshift(freqs, axes=(0, 1)))
    self.assertAllEqual(
        fft_ops.ifftshift(shifted, axes=(0, 1)),
        np.fft.ifftshift(shifted, axes=(0, 1)))
