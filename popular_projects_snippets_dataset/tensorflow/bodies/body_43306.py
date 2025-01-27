# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py

fn_has_kwargs = lambda **x: x
self.assertTrue(function_utils.has_kwargs(fn_has_kwargs))

fn_has_no_kwargs = lambda x: x
self.assertFalse(function_utils.has_kwargs(fn_has_no_kwargs))
