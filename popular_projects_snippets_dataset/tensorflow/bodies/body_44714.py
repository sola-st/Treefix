# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
with self._basic_function_scope() as test_scope:
    exit(py_builtins.globals_in_original_context(test_scope))
