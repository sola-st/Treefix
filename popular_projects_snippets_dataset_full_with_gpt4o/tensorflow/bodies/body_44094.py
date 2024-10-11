# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_function_call_test.py
self.skipTest('fix static analysis for nested classes')
n = type_(n)
self.assertFunctionMatchesEager(while_with_method_closure_call, n)
