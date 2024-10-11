# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with context.eager_mode():
    variable_scope.get_variable("v1", [], trainable=True)
    variable_scope.get_variable("v2", [], trainable=False)
    self.assertFalse(ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES))
    self.assertFalse(ops.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES))
