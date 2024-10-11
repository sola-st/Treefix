# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    with variable_scope.variable_scope("default") as default:
        with variable_scope.variable_scope(None, "layer"):
            self.assertEqual(
                variable_scope.get_variable("w", []).name, "default/layer/w:0")
        with variable_scope.variable_scope(None, "layer"):
            self.assertEqual(
                variable_scope.get_variable("w", []).name,
                "default/layer_1/w:0")
        with variable_scope.variable_scope(default):
            pass
        # No matter the jump in the middle, unique numbering continues.
        with variable_scope.variable_scope(None, "layer"):
            self.assertEqual(
                variable_scope.get_variable("w", []).name,
                "default/layer_2/w:0")
