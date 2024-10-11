# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
a = 10.0
b = [11.0, 100.0]
uniform = uniform_lib.Uniform(a, b)
self.assertTrue(
    self.evaluate(
        math_ops.reduce_all(uniform.prob(uniform.sample(10)) > 0)))
