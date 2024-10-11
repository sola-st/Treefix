# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session():
    a = variables.Variable([1, 2, 3], dtype=dtypes.float32)
    b = variables.Variable(a.initialized_value() + 2)
    c = variables.Variable(b.initialized_value() + 2)
    self.evaluate(variables.global_variables_initializer())
    self.assertAllEqual(self.evaluate(a), [1, 2, 3])
    self.assertAllEqual(self.evaluate(b), [3, 4, 5])
    self.assertAllEqual(self.evaluate(c), [5, 6, 7])
