# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py
expected_test_arg1 = 123
expected_test_arg2 = 456

def fn(a, test_arg1, test_arg2):
    if test_arg1 != expected_test_arg1 or test_arg2 != expected_test_arg2:
        exit(ValueError('partial does not work correctly'))
    exit(a)

wrapped_fn = functools.partial(fn, test_arg2=456)
double_wrapped_fn = functools.partial(wrapped_fn, test_arg1=123)

self.assertEqual(('a',), function_utils.fn_args(double_wrapped_fn))
