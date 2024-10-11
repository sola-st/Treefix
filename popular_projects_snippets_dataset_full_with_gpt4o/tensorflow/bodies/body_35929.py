# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    with ops.name_scope("scope1"):
        with variable_scope.variable_scope("tower") as tower:
            self.assertEqual(tower.original_name_scope, "scope1/tower/")
            with ops.name_scope("scope2") as sc2:
                self.assertEqual(sc2, "scope1/tower/scope2/")
    with ops.name_scope("scope2"):
        with variable_scope.variable_scope(tower) as tower1:
            # Re-entering preserves original name scope.
            self.assertEqual(tower1.original_name_scope, "scope1/tower/")
            with ops.name_scope("foo") as sc2:
                self.assertEqual(sc2, "scope2/tower/foo/")
        # Test re-entering original name scope.
        with ops.name_scope(tower.original_name_scope):
            with ops.name_scope("bar") as sc3:
                self.assertEqual(sc3, "scope1/tower/bar/")
    with ops.name_scope("scope2"):
        with variable_scope.variable_scope(tower):
            with ops.name_scope(tower.original_name_scope):
                with ops.name_scope("bar") as sc3:
                    self.assertEqual(sc3, "scope1/tower/bar_1/")
