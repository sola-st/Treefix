# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
with test_case_self._basic_function_scope() as test_scope:
    # Oddly, it's sufficient to use `self` in an inner function
    # to gain access to __class__ in this scope.
    # TODO(mdan): Is this true across implementations?
    # Note: normally, it's illegal to use super() in inner functions (it
    # throws an error), but the generated code may create them.
    l = lambda: py_builtins.super_in_original_context(  # pylint:disable=g-long-lambda
        super, (), test_scope).overridden_method(x)
    exit(l())
