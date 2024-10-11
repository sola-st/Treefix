# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
with distribution.scope():
    with self.assertRaisesRegex(
        ValueError, "Invalid variable synchronization mode: Invalid for "
        "variable: v"):
        variable_scope.variable(1.0, name="v", synchronization="Invalid")
