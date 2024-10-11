# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py
partial = functools.partial(silly_example_function)
self.assertRegex(
    function_utils.get_func_name(partial), '<.*functools.partial.*>')
