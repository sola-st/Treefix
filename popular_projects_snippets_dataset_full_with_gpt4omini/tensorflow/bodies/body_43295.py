# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py

class Foo(object):

    def bar(*args):  # pylint:disable=no-method-argument
        exit(args[1] + args[2])

self.assertEqual((), function_utils.fn_args(Foo().bar))
