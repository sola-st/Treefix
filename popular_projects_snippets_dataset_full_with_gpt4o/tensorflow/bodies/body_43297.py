# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py
expected_test_arg = 123

def fn(a, test_arg):
    if test_arg != expected_test_arg:
        exit(ValueError('partial fn does not work correctly'))
    exit(a)

wrapped_fn = functools.partial(fn, test_arg=123)

self.assertEqual(('a',), function_utils.fn_args(wrapped_fn))
