# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    with variable_scope.variable_scope("outer") as outer:
        with variable_scope.variable_scope(outer):
            self.assertEqual(
                variable_scope.get_variable("w", []).name, "outer/w:0")
            with ops.name_scope("scope2") as sc2:
                self.assertEqual(sc2, "outer/outer/scope2/")
        with variable_scope.variable_scope("default"):
            self.assertEqual(
                variable_scope.get_variable("w", []).name, "outer/default/w:0")
            with ops.name_scope("scope2") as sc2:
                self.assertEqual(sc2, "outer/default/scope2/")

        with variable_scope.variable_scope(outer, reuse=True):
            self.assertEqual(
                variable_scope.get_variable("w", []).name, "outer/w:0")
            with ops.name_scope("scope2") as sc2:
                self.assertEqual(sc2, "outer/outer_1/scope2/")
        with variable_scope.variable_scope("default", reuse=True):
            self.assertEqual(
                variable_scope.get_variable("w", []).name, "outer/default/w:0")
            with ops.name_scope("scope2") as sc2:
                self.assertEqual(sc2, "outer/default_1/scope2/")
