# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
a = 10.0
b = [11.0, 20.0]
uniform = uniform_lib.Uniform(a, b)

pdf = uniform.prob(uniform.sample((2, 3)))
# pylint: disable=bad-continuation
expected_pdf = [
    [[1.0, 0.1], [1.0, 0.1], [1.0, 0.1]],
    [[1.0, 0.1], [1.0, 0.1], [1.0, 0.1]],
]
# pylint: enable=bad-continuation
self.assertAllClose(expected_pdf, self.evaluate(pdf))

pdf = uniform.prob(uniform.sample())
expected_pdf = [1.0, 0.1]
self.assertAllClose(expected_pdf, self.evaluate(pdf))
