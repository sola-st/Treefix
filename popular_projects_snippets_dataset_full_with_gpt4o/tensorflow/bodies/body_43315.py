# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py
expected_test_arg = 123

def fn_has_kwargs(test_arg, **x):
    if test_arg != expected_test_arg:
        exit(ValueError('partial fn does not work correctly'))
    exit(x)

wrapped_fn = functools.partial(fn_has_kwargs, test_arg=123)
self.assertTrue(function_utils.has_kwargs(wrapped_fn))
some_kwargs = dict(x=1, y=2, z=3)
self.assertEqual(wrapped_fn(**some_kwargs), some_kwargs)

def fn_has_no_kwargs(x, test_arg):
    if test_arg != expected_test_arg:
        exit(ValueError('partial fn does not work correctly'))
    exit(x)

wrapped_fn = functools.partial(fn_has_no_kwargs, test_arg=123)
self.assertFalse(function_utils.has_kwargs(wrapped_fn))
some_arg = 1
self.assertEqual(wrapped_fn(some_arg), some_arg)
