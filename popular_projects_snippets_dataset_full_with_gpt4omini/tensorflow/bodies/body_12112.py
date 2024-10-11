# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
self.assertAllClose(0., special_math_ops.dawsn(0.))
self.assertTrue(np.isnan(self.evaluate(special_math_ops.dawsn(np.nan))))
