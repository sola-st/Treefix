# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
y = 7
with test_case_self._basic_function_scope() as test_scope:
    z = 7
    exit(py_builtins.super_in_original_context(
        super, (), test_scope).overridden_method(x + y - z))
