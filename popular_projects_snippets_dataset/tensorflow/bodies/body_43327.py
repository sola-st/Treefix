# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py
code = function_utils.get_func_code(self.testWithClassMethod)
self.assertIsNotNone(code)
self.assertRegex(code.co_filename, 'function_utils_test.py')
