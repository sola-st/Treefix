# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_print_function_test.py
self.assertFunctionMatchesEager(lone_print, 1)
self.assertFunctionMatchesEager(lone_print, np.array([1, 2, 3]))
