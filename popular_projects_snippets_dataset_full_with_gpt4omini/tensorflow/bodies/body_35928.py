# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with ops.name_scope("testVarScopeNameScope1"):
    with variable_scope.variable_scope("tower") as tower:
        with ops.name_scope("scope2") as sc2:
            self.assertEqual(sc2, "testVarScopeNameScope1/tower/scope2/")
    if not context.executing_eagerly():
        with variable_scope.variable_scope(
            tower):  # Re-entering acts like another "tower".
            with ops.name_scope("scope2") as sc2:
                self.assertEqual(sc2, "testVarScopeNameScope1/tower_1/scope2/")
        with variable_scope.variable_scope(
            "tower"):  # Re-entering by string acts the same.
            with ops.name_scope("scope2") as sc2:
                self.assertEqual(sc2, "testVarScopeNameScope1/tower_2/scope2/")

with ops.name_scope("testVarScopeNameScope2"):
    with variable_scope.variable_scope("tower"):
        with ops.name_scope("scope2") as sc2:
            self.assertEqual(sc2, "testVarScopeNameScope2/tower/scope2/")
    if not context.executing_eagerly():
        with variable_scope.variable_scope(tower):
            with ops.name_scope("scope2") as sc2:
                self.assertEqual(sc2, "testVarScopeNameScope2/tower_1/scope2/")

root_var_scope = variable_scope.get_variable_scope()
with ops.name_scope("testVarScopeNameScope3"):
    with variable_scope.variable_scope(root_var_scope):
        with ops.name_scope("scope2") as sc2:
            self.assertEqual(sc2, "testVarScopeNameScope3/scope2/")
