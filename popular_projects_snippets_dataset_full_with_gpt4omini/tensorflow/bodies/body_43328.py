# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py
callable_instance = SillyCallableClass()
code = function_utils.get_func_code(callable_instance)
self.assertIsNotNone(code)
self.assertRegex(code.co_filename, 'function_utils_test.py')
