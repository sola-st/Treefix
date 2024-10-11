# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
spectrum = [[3., 2., 1.], [2., 1.5, 1.]]
with self.cached_session():
    operator = linalg.LinearOperatorCirculant(spectrum)
    h = operator.convolution_kernel()
    c = operator.to_dense()

    self.assertAllEqual((2, 3), h.shape)
    self.assertAllEqual((2, 3, 3), c.shape)
    self.assertAllClose(self.evaluate(h), self.evaluate(c)[:, :, 0])
