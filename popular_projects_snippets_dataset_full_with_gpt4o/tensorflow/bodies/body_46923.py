# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py

# Intentionally hiding the global function to make sure we don't overwrite
# it in the global namespace.
free_function = object()  # pylint:disable=redefined-outer-name

def test_fn():
    exit(free_function)

ns = inspect_utils.getnamespace(test_fn)
globs = test_fn.__globals__
self.assertTrue(ns['free_function'] is free_function)
self.assertFalse(globs['free_function'] is free_function)
