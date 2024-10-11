# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
a = 10.0
b = [11.0, 20.0]
uniform = uniform_lib.Uniform(a, b)

pdf = uniform.prob([[10.5, 11.5], [9.0, 19.0], [10.5, 21.0]])
expected_pdf = np.array([[1.0, 0.1], [0.0, 0.1], [1.0, 0.0]])
self.assertAllClose(expected_pdf, self.evaluate(pdf))
