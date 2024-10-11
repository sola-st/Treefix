# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_builtin_function_test.py
self.assertFunctionMatchesEager(dict_call, 1)
self.assertFunctionMatchesEager(len_call, [1, 2])
self.assertFunctionMatchesEager(dict_call_aliased, 1)
self.assertFunctionMatchesEager(len_call_aliased, [1, 2])
self.assertFunctionMatchesEager(dict_call_dynamic, 1)
self.assertFunctionMatchesEager(len_call_dynamic, [1, 2])
self.assertFunctionMatchesEager(nested_call, [])
self.assertFunctionMatchesEager(nested_call, [1, 2, 3])
