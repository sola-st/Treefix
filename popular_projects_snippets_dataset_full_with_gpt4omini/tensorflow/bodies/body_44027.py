# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_print_function_test.py
self.assertFunctionMatchesEager(multiple_prints, 1, 2)
self.assertFunctionMatchesEager(multiple_prints, np.array([1, 2, 3]), 4)
