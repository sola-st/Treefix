# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session():
    var_x = variables.VariableV1(2.0)
    var_y = variables.VariableV1(2.0, trainable=False)
    var_z = variables.VariableV1(2.0, trainable=True)
    var_t = variables.VariableV1(
        2.0,
        trainable=True,
        collections=[
            ops.GraphKeys.TRAINABLE_VARIABLES, ops.GraphKeys.GLOBAL_VARIABLES
        ])
    self.assertEqual([var_x, var_y, var_z, var_t],
                     variables.global_variables())
    self.assertEqual([var_x, var_z, var_t], variables.trainable_variables())
