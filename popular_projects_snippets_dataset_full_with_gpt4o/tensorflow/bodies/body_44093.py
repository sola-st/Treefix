# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_function_call_test.py
l = type_(l)
self.assertFunctionMatchesEager(for_with_lambda_closure_call, l)
