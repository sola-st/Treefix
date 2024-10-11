# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
self.assertAllClose(np.pi**2 / 6., special_math_ops.spence(0.))
self.assertAllClose(0., special_math_ops.spence(1.))
self.assertTrue(np.isnan(self.evaluate(special_math_ops.spence(np.nan))))
# Check that the domain of definition is [0, inf)
self.assertTrue(
    np.all(
        np.isnan(
            self.evaluate(
                special_math_ops.spence(
                    np.random.uniform(-20., -1., size=int(1e3)))))))
