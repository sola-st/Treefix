# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_print_function_test.py
self.assertFunctionMatchesEager(print_in_cond, 0)
self.assertFunctionMatchesEager(print_in_cond, 1)
