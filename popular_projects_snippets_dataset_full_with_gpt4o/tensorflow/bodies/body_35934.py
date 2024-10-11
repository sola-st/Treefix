# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    with variable_scope.variable_scope(None, "defaultScope1"):
        with variable_scope.variable_scope(None, "layer"):
            self.assertEqual(
                variable_scope.get_variable("w", []).name,
                "defaultScope1/layer/w:0")
    with variable_scope.variable_scope(None, "defaultScope1"):
        with variable_scope.variable_scope(None, "layer"):
            self.assertEqual(
                variable_scope.get_variable("w", []).name,
                "defaultScope1_1/layer/w:0")
    with variable_scope.variable_scope(None, "defaultScope"):
        with variable_scope.variable_scope(None, "layer"):
            self.assertEqual(
                variable_scope.get_variable("w", []).name,
                "defaultScope/layer/w:0")
    with variable_scope.variable_scope(None, "defaultScope1"):
        with variable_scope.variable_scope(None, "layer"):
            self.assertEqual(
                variable_scope.get_variable("w", []).name,
                "defaultScope1_2/layer/w:0")
