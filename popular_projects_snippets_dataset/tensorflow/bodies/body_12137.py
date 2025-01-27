# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
self.assertAllClose(1., special_math_ops.bessel_j0(0.))
self.assertAllClose(0., special_math_ops.bessel_j1(0.))
self.assertTrue(np.isnan(self.evaluate(special_math_ops.bessel_j0(np.nan))))
self.assertTrue(np.isnan(self.evaluate(special_math_ops.bessel_j1(np.nan))))
