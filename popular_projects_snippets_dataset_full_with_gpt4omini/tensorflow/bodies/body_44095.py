# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_function_call_test.py
self.skipTest('fix static analysis for nested classes')
l = type_(l)
self.assertFunctionMatchesEager(for_with_method_closure_call, l)
