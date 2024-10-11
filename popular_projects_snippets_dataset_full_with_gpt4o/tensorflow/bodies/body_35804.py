# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session():
    var_x = variables.Variable(2.0)
    var_y = variables.Variable(3.0)
    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose(2.0, self.evaluate(var_x))
    self.assertAllClose(3.0, self.evaluate(var_y))
    self.assertAllClose(5.0, self.evaluate(math_ops.add(var_x, var_y)))
