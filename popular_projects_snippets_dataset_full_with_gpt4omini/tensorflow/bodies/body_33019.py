# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
# Non-invertible inputs result in lower-triangular NaNs.
x = constant_op.constant([[1., -1., 0.], [-1., 1., -1.], [0., -1., 1.]])
chol = linalg_ops.cholesky(x)
# Extract the lower-triangular elements.
lower_mask = array_ops.matrix_band_part(
    constant_op.constant(True, shape=x.shape), -1, 0)
chol_lower = array_ops.boolean_mask(chol, lower_mask)
# Assert all NaN.
all_nan = self.evaluate(
    math_ops.reduce_all(math_ops.reduce_all(math_ops.is_nan(chol_lower))))
self.assertTrue(all_nan)
