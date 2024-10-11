# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
with self.session():
    x = [0, 1, 2, 3, 4, -4, -3, -2, -1]
    y = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    self.assertAllEqual(fft_ops.fftshift(x), y)
    self.assertAllEqual(fft_ops.ifftshift(y), x)
    x = [0, 1, 2, 3, 4, -5, -4, -3, -2, -1]
    y = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
    self.assertAllEqual(fft_ops.fftshift(x), y)
    self.assertAllEqual(fft_ops.ifftshift(y), x)
