# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    with ops.name_scope("testVarOpScope1"):
        with variable_scope.variable_scope("tower", "default", []):
            self.assertEqual(
                variable_scope.get_variable("w", []).name, "tower/w:0")
            with ops.name_scope("testVarOpScope2") as sc2:
                self.assertEqual(sc2, "testVarOpScope1/tower/testVarOpScope2/")
        with variable_scope.variable_scope("tower", "default", []):
            with self.assertRaises(ValueError):
                variable_scope.get_variable("w", [])
            with ops.name_scope("testVarOpScope2") as sc2:
                self.assertEqual(sc2, "testVarOpScope1/tower_1/testVarOpScope2/")

    with ops.name_scope("testVarOpScope2"):
        with variable_scope.variable_scope(None, "default", []):
            self.assertEqual(
                variable_scope.get_variable("w", []).name, "default/w:0")
            with ops.name_scope("testVarOpScope2") as sc2:
                self.assertEqual(sc2, "testVarOpScope2/default/testVarOpScope2/")
        with variable_scope.variable_scope(None, "default", []):
            self.assertEqual(
                variable_scope.get_variable("w", []).name, "default_1/w:0")
            with ops.name_scope("testVarOpScope2") as sc2:
                self.assertEqual(sc2, "testVarOpScope2/default_1/testVarOpScope2/")
