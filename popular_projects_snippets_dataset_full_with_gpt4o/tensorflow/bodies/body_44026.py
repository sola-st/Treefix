# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_print_function_test.py
self.assertFunctionMatchesEager(print_multiple_values, 1)
self.assertFunctionMatchesEager(print_multiple_values, np.array([1, 2, 3]))
