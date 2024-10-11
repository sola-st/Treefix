# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
a_v = np.array([1.0, 1.0, 1.0], dtype=np.float32)
b_v = np.array([1.0, 2.0, 3.0], dtype=np.float32)

with self.assertRaisesWithPredicateMatch(errors.InvalidArgumentError,
                                         "x < y"):
    uniform = uniform_lib.Uniform(low=a_v, high=b_v, validate_args=True)
    self.evaluate(uniform.low)
