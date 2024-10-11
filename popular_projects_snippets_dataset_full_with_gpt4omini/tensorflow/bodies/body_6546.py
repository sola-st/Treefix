# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
with distribution.scope():
    with self.assertRaisesRegex(
        ValueError, "`NONE` variable synchronization mode is not "
        "supported with "):
        variable_scope.variable(
            1.0,
            name="v",
            synchronization=variable_scope.VariableSynchronization.NONE)
