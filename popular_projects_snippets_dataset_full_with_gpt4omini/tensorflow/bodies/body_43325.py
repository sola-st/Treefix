# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py
with self.assertRaises(ValueError):
    function_utils.get_func_name(None)
