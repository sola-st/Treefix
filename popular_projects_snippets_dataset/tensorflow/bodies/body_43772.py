# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_user_function_test.py
self.assertFunctionMatchesEager(static_fn, 1)
self.assertFunctionMatchesEager(factory_dynamic_fn, 1)
self.assertFunctionMatchesEager(param_dynamic_fn, function_1, 1)
self.assertFunctionMatchesEager(variable_dynamic_fn, 1)
self.assertFunctionMatchesEager(variable_dynamic_whitelisted_fn, 1)
self.assertFunctionMatchesEager(dynamic_fn_with_kwargs, function_1, 1)
