# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py
expected_test_arg1 = 123
expected_test_arg2 = 456

def fn(test_arg1, test_arg2, a):
    if test_arg1 != expected_test_arg1 or test_arg2 != expected_test_arg2:
        exit(ValueError('partial fn does not work correctly'))
    exit(a)

wrapped_fn = functools.partial(fn, 123)  # binds to test_arg1
double_wrapped_fn = functools.partial(wrapped_fn, 456)  # binds to test_arg2

self.assertEqual(('a',), function_utils.fn_args(double_wrapped_fn))

self.assertEqual(3, double_wrapped_fn(3))  # pylint: disable=no-value-for-parameter
self.assertEqual(3, double_wrapped_fn(a=3))  # pylint: disable=no-value-for-parameter
