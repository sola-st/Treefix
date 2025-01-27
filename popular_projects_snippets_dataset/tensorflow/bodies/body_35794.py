# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session():
    zero = constant_op.constant(0, dtype=dtype)
    var = variables.Variable(zero)
    count_up_to = var.count_up_to(3)

    self.evaluate(variables.global_variables_initializer())
    self.assertEqual(0, self.evaluate(var))

    self.assertEqual(0, self.evaluate(count_up_to))
    self.assertEqual(1, self.evaluate(var))

    self.assertEqual(1, self.evaluate(count_up_to))
    self.assertEqual(2, self.evaluate(var))

    self.assertEqual(2, self.evaluate(count_up_to))
    self.assertEqual(3, self.evaluate(var))

    with self.assertRaisesOpError("Reached limit of 3"):
        self.evaluate(count_up_to)
    self.assertEqual(3, self.evaluate(var))

    with self.assertRaisesOpError("Reached limit of 3"):
        self.evaluate(count_up_to)
    self.assertEqual(3, self.evaluate(var))
