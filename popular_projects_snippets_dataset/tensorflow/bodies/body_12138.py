# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
self.assertTrue(np.isinf(self.evaluate(special_math_ops.bessel_k0(0.))))
self.assertTrue(np.isinf(self.evaluate(special_math_ops.bessel_k0e(0.))))
self.assertTrue(np.isinf(self.evaluate(special_math_ops.bessel_k1(0.))))
self.assertTrue(np.isinf(self.evaluate(special_math_ops.bessel_k1e(0.))))
self.assertTrue(np.isnan(self.evaluate(special_math_ops.bessel_k0(np.nan))))
self.assertTrue(
    np.isnan(self.evaluate(special_math_ops.bessel_k0e(np.nan))))
self.assertTrue(np.isnan(self.evaluate(special_math_ops.bessel_k1(np.nan))))
self.assertTrue(
    np.isnan(self.evaluate(special_math_ops.bessel_k1e(np.nan))))
