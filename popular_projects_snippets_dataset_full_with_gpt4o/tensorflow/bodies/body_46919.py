# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py
ns = inspect_utils.getnamespace(factory)
self.assertEqual(ns['free_function'], free_function)
