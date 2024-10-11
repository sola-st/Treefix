# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session():
    var = variables.Variable(0.0)
    plus_one = var.assign_add(1.0)
    minus_one = var.assign_sub(2.0)
    four = var.assign(4.0)
    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose(0.0, self.evaluate(var))

    self.assertAllClose(1.0, self.evaluate(plus_one))
    self.assertAllClose(1.0, self.evaluate(var))

    self.assertAllClose(-1.0, self.evaluate(minus_one))
    self.assertAllClose(-1.0, self.evaluate(var))

    self.assertAllClose(4.0, self.evaluate(four))
    self.assertAllClose(4.0, self.evaluate(var))
