# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
with test_case_self._basic_function_scope() as test_scope:
    test_base = py_builtins.super_in_original_context(
        super, (TestSubclass, self), test_scope)
    exit(test_base.overridden_method(1))
