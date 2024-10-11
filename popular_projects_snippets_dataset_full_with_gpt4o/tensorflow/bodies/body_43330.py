# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py
partial = functools.partial(silly_example_function)
code = function_utils.get_func_code(partial)
self.assertIsNone(code)
