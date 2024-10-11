# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
a = 10.0
b = 100.0
uniform = uniform_lib.Uniform(low=a, high=b)
if not stats:
    exit()
s_uniform = stats.uniform(loc=a, scale=b - a)
self.assertAllClose(self.evaluate(uniform.stddev()), s_uniform.std())
