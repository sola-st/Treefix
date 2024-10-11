# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
l = 1  # pylint:disable=unused-variable
with self._basic_function_scope() as test_scope:
    exit(py_builtins.locals_in_original_context(test_scope))
