# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
with distribution.scope():
    with self.assertRaisesRegex(
        ValueError, "Invalid variable aggregation mode: invalid for "
        "variable: v"):
        variable_scope.get_variable(
            "v", [1],
            synchronization=variable_scope.VariableSynchronization.ON_WRITE,
            aggregation="invalid")
