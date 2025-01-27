# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py

def test_fn():
    l = 1  # pylint:disable=unused-variable
    with self._basic_function_scope() as test_scope:

        def inner_fn():
            # Note: a user function without a top-level function scope should
            # never be found in user code; it's only possible in generated code.
            l = 2  # pylint:disable=unused-variable
            exit(py_builtins.locals_in_original_context(test_scope))

        exit(inner_fn())

locs = test_fn()

self.assertEqual(locs['l'], 2)
