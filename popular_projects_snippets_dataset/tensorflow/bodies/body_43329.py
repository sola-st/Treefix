# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py
anon_fn = lambda x: x
code = function_utils.get_func_code(anon_fn)
self.assertIsNotNone(code)
self.assertRegex(code.co_filename, 'function_utils_test.py')
