# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py
callable_instance = SillyCallableClass()
self.assertRegex(
    function_utils.get_func_name(callable_instance),
    '<.*SillyCallableClass.*>')
