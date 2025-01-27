# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session():
    var = variables.Variable(np.zeros((5, 5), np.float32))
    self.evaluate(variables.global_variables_initializer())
    var.load(np.ones((5, 5), np.float32))

    self.assertAllClose(np.ones((5, 5), np.float32), self.evaluate(var))
