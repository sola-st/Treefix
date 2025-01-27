# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with variable_scope.variable_scope("tower4") as tower:
    self.assertEqual(tower.name, "tower4")
    with ops.name_scope("scope") as sc:
        self.assertEqual(sc, "tower4/scope/")

with variable_scope.variable_scope("tower5"):
    with variable_scope.variable_scope("bar") as bar:
        self.assertEqual(bar.name, "tower5/bar")
        with ops.name_scope("scope") as sc:
            self.assertEqual(sc, "tower5/bar/scope/")

with variable_scope.variable_scope("tower6"):
    with variable_scope.variable_scope(tower, reuse=True) as tower_shared:
        self.assertEqual(tower_shared.name, "tower4")
        with ops.name_scope("scope") as sc:
            self.assertEqual(sc, "tower6/tower4/scope/")
