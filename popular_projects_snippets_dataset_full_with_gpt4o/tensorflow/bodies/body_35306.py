# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
a = constant_op.constant([0.0, 5.0])
b = constant_op.constant(10.0)
uniform = uniform_lib.Uniform(low=a, high=b)

x = np.array([0.0, 8.0], dtype=np.float32)
expected_pdf = np.array([1.0 / (10.0 - 0.0), 1.0 / (10.0 - 5.0)])

pdf = uniform.prob(x)
self.assertAllClose(expected_pdf, self.evaluate(pdf))
