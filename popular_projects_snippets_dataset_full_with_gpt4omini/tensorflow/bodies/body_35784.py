# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session():
    var0 = variables.VariableV1(0.0)
    self.assertEqual("Variable:0", var0.name)
    self.assertEqual("Variable", var0._shared_name)
    self.assertEqual([], var0.get_shape())
    self.assertEqual([], var0.get_shape())
    self.assertEqual([], var0.shape)

    var1 = variables.VariableV1(1.1)
    self.assertEqual("Variable_1:0", var1.name)
    self.assertEqual("Variable_1", var1._shared_name)
    self.assertEqual([], var1.get_shape())
    self.assertEqual([], var1.get_shape())
    self.assertEqual([], var1.shape)

    with self.assertRaisesOpError("Attempting to use uninitialized value"):
        self.evaluate(var0)

    with self.assertRaisesOpError("Attempting to use uninitialized value"):
        self.evaluate(var1)

    self.evaluate(variables.global_variables_initializer())

    self.assertAllClose(0.0, self.evaluate(var0))
    self.assertAllClose(1.1, self.evaluate(var1))
