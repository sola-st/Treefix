# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
# Check that local variable respects naming.
with variable_scope.variable_scope("outer") as outer:
    with variable_scope.variable_scope(outer, "default", []):
        local_var = variable_scope.get_local_variable(
            "w", [], collections=["foo"])
        self.assertEqual(local_var.name, "outer/w:0")

if not context.executing_eagerly():
    # Since variable is local, it should be in the local variable collection
    # but not the trainable collection.
    self.assertIn(local_var,
                  ops.get_collection(ops.GraphKeys.LOCAL_VARIABLES))
    self.assertIn(local_var, ops.get_collection("foo"))
    self.assertNotIn(local_var,
                     ops.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES))
    # Check that local variable respects `reuse`.
    with variable_scope.variable_scope(outer, "default", reuse=True):
        self.assertEqual(
            variable_scope.get_local_variable("w", []).name, "outer/w:0")
