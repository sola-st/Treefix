# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
spectrum = math_ops.cast([[6. + 0j, 4 + 0j], [2j, 3. + 0j]],
                         dtypes.complex64)
operator = linalg.LinearOperatorCirculant2D(spectrum)
with self.cached_session():
    with self.assertRaisesOpError("Not positive definite"):
        self.evaluate(operator.assert_positive_definite())
