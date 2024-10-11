# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    with self.assertRaisesRegex(TypeError, "auxiliary_name_scope"):
        with variable_scope.variable_scope(
            None, default_name="scope", auxiliary_name_scope="invalid"):
            pass

    with self.assertRaisesRegex(TypeError, "auxiliary_name_scope"):
        with variable_scope.variable_scope(
            "scope", auxiliary_name_scope="invalid"):
            pass

    with variable_scope.variable_scope("scope") as scope:
        pass
    with self.assertRaisesRegex(TypeError, "auxiliary_name_scope"):
        with variable_scope.variable_scope(
            scope, auxiliary_name_scope="invalid"):
            pass
