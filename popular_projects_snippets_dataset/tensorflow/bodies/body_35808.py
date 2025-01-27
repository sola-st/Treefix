# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session():
    with ops.name_scope("scope_1"):
        var_x = variables.VariableV1(2.0)
    with ops.name_scope("scope_2"):
        var_y = variables.VariableV1(2.0)

    self.assertEqual([var_x, var_y], variables.global_variables())
    self.assertEqual([var_x], variables.global_variables("scope_1"))
    self.assertEqual([var_y], variables.global_variables("scope_2"))

    self.assertEqual([var_x, var_y], variables.trainable_variables())
    self.assertEqual([var_x], variables.trainable_variables("scope_1"))
    self.assertEqual([var_y], variables.trainable_variables("scope_2"))
