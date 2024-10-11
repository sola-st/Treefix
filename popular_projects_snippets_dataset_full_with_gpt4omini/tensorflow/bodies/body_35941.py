# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    with self.assertRaises(ValueError):
        with variable_scope.variable_scope(None, "default", reuse=True):
            self.assertEqual(
                variable_scope.get_variable("w", []).name, "outer/tower/w:0")
