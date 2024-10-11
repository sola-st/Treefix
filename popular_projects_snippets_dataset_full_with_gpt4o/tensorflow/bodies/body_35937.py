# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    with variable_scope.variable_scope("root"):
        with variable_scope.variable_scope("towerA") as tower_a:
            va = variable_scope.get_variable("v", [1])
            self.assertEqual(va.name, "root/towerA/v:0")

        with variable_scope.variable_scope(tower_a, reuse=True):
            va2 = variable_scope.get_variable("v", [1])
            self.assertIs(va2, va)

        with variable_scope.variable_scope("towerB"):
            vb = variable_scope.get_variable("v", [1])
            self.assertEqual(vb.name, "root/towerB/v:0")

        with self.assertRaises(ValueError):
            with variable_scope.variable_scope("towerA"):
                va2 = variable_scope.get_variable("v", [1])

        with variable_scope.variable_scope("towerA", reuse=True):
            va2 = variable_scope.get_variable("v", [1])
            self.assertIs(va2, va)

        with variable_scope.variable_scope("foo"):
            with variable_scope.variable_scope("bar"):
                v = variable_scope.get_variable("v", [1])
                self.assertEqual(v.name, "root/foo/bar/v:0")
                with variable_scope.variable_scope(tower_a, reuse=True):
                    va3 = variable_scope.get_variable("v", [1])
                    self.assertIs(va, va3)

        with self.assertRaises(ValueError):
            with variable_scope.variable_scope(tower_a, reuse=True):
                with variable_scope.variable_scope("baz"):
                    variable_scope.get_variable("v", [1])

        with self.assertRaises(ValueError) as exc:
            with variable_scope.variable_scope(tower_a, reuse=True):
                variable_scope.get_variable("v", [2])  # Different shape.
        self.assertEqual("shape" in str(exc.exception), True)

        with self.assertRaises(ValueError) as exc:
            with variable_scope.variable_scope(tower_a, reuse=True):
                variable_scope.get_variable("v", [1], dtype=dtypes.int32)
        self.assertEqual("dtype" in str(exc.exception), True)
