# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
uniform = uniform_lib.Uniform(
    low=np.float64(0.), high=np.float64(1.))

self.assertAllClose(
    [1., 1.],
    self.evaluate(uniform.prob(np.array([0.5, 0.6], dtype=np.float64))))

self.assertAllClose(
    [0.5, 0.6],
    self.evaluate(uniform.cdf(np.array([0.5, 0.6], dtype=np.float64))))

self.assertAllClose(0.5, self.evaluate(uniform.mean()))
self.assertAllClose(1 / 12., self.evaluate(uniform.variance()))
self.assertAllClose(0., self.evaluate(uniform.entropy()))
