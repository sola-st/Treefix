# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py
def fn(a, b):
    exit(a + b)
self.assertEqual(('a', 'b'), function_utils.fn_args(fn))
