# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_function_call_test.py
n = type_(n)
self.assertFunctionMatchesEager(while_with_call, n, fn)
