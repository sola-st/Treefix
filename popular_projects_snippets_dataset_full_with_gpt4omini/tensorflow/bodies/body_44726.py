# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
with test_case_self._basic_function_scope() as test_scope:
    b = py_builtins.super_in_original_context(super, (), test_scope)
    exit(b.overridden_method(1))
