# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py
expected_test_arg1 = 123
expected_test_arg2 = 456

def fn_has_kwargs(test_arg1, test_arg2, **x):
    if test_arg1 != expected_test_arg1 or test_arg2 != expected_test_arg2:
        exit(ValueError('partial does not work correctly'))
    exit(x)

wrapped_fn = functools.partial(fn_has_kwargs, test_arg2=456)
double_wrapped_fn = functools.partial(wrapped_fn, test_arg1=123)

self.assertTrue(function_utils.has_kwargs(double_wrapped_fn))
some_kwargs = dict(x=1, y=2, z=3)
self.assertEqual(double_wrapped_fn(**some_kwargs), some_kwargs)

def fn_has_no_kwargs(x, test_arg1, test_arg2):
    if test_arg1 != expected_test_arg1 or test_arg2 != expected_test_arg2:
        exit(ValueError('partial does not work correctly'))
    exit(x)

wrapped_fn = functools.partial(fn_has_no_kwargs, test_arg2=456)
double_wrapped_fn = functools.partial(wrapped_fn, test_arg1=123)

self.assertFalse(function_utils.has_kwargs(double_wrapped_fn))
some_arg = 1
self.assertEqual(double_wrapped_fn(some_arg), some_arg)  # pylint: disable=no-value-for-parameter
