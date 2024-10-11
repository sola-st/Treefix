# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    with variable_scope.variable_scope("outer") as outer:
        pass
    with variable_scope.variable_scope(outer, "default", []):
        self.assertEqual(
            variable_scope.get_variable("w", []).name, "outer/w:0")
        with ops.name_scope("scope2") as sc2:
            self.assertEqual(sc2, "outer_1/scope2/")
        with variable_scope.variable_scope(None, "default", []):
            self.assertEqual(
                variable_scope.get_variable("w", []).name, "outer/default/w:0")
            with ops.name_scope("scope2") as sc2:
                self.assertEqual(sc2, "outer_1/default/scope2/")

    with variable_scope.variable_scope(outer, "default", reuse=True):
        self.assertEqual(
            variable_scope.get_variable("w", []).name, "outer/w:0")
        with ops.name_scope("scope2") as sc2:
            self.assertEqual(sc2, "outer_2/scope2/")
        outer.reuse_variables()
        with variable_scope.variable_scope(None, "default", []):
            self.assertEqual(
                variable_scope.get_variable("w", []).name, "outer/default/w:0")
            with ops.name_scope("scope2") as sc2:
                self.assertEqual(sc2, "outer_2/default/scope2/")
