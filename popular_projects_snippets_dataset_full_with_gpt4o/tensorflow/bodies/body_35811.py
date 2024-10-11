# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session() as sess:
    var = variables.Variable([1, 12])
    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose([1, 12], self.evaluate(var))
