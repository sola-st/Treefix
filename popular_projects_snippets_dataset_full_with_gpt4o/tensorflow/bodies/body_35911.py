# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
store = variable_scope.EagerVariableStore()
with store.as_default():
    trainable = variable_scope.get_variable("v1", [], trainable=True)
    not_trainable = variable_scope.get_variable("v2", [], trainable=False)
    concat = variable_scope.get_variable(
        "v3", [], collections=[ops.GraphKeys.CONCATENATED_VARIABLES])
    self.assertEqual(
        ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES),
        [trainable, not_trainable])
    self.assertEqual(
        ops.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES),
        [trainable, concat])
    self.assertEqual(
        ops.get_collection(ops.GraphKeys.CONCATENATED_VARIABLES), [concat])
