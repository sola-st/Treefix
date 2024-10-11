# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
a_v = np.array([1.0, 1.0, 1.0])
b_v = np.array([[1.5, 2.0, 3.0]])
uniform = uniform_lib.Uniform(low=a_v, high=b_v)

expected_entropy = np.log(b_v - a_v)
self.assertAllClose(expected_entropy, self.evaluate(uniform.entropy()))
