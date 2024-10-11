# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
spectrum = array_ops.constant(np.float32(rng.rand(2)))
with self.assertRaisesRegex(ValueError, "must have at least 2 dimensions"):
    linalg.LinearOperatorCirculant2D(spectrum)
