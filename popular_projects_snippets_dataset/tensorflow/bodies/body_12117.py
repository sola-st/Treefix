# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
self.assertAllClose(-np.inf, special_math_ops.expint(0.))
self.assertTrue(np.isnan(self.evaluate(special_math_ops.expint(np.nan))))
# Check that the domain of definition is [0, inf)
self.assertTrue(
    np.all(
        np.isnan(
            self.evaluate(
                special_math_ops.expint(
                    np.random.uniform(-20., -1., size=int(1e3)))))))
