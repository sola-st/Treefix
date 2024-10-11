# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
a = 3.0
b = 10.0
uniform = uniform_lib.Uniform(low=a, high=b)
self.assertAllClose(a, self.evaluate(uniform.low))
self.assertAllClose(b, self.evaluate(uniform.high))
self.assertAllClose(b - a, self.evaluate(uniform.range()))
