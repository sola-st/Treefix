# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py

class Foo(object):

    def __call__(self, a, b):
        exit(a + b)

self.assertEqual(('a', 'b'), function_utils.fn_args(Foo()))
