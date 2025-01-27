# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with variable_scope.variable_scope("aa"):
    scope = variable_scope.variable_scope("bb")
    scope.__enter__()
    with variable_scope.variable_scope("cc"):
        with self.assertRaises(RuntimeError):
            scope.__exit__(None, None, None)
    scope.__exit__(None, None, None)
