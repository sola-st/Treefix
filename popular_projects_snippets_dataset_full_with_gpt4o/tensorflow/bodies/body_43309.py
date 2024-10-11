# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py

class FooHasKwargs(object):

    def __call__(self, **x):
        del x
self.assertTrue(function_utils.has_kwargs(FooHasKwargs()))

class FooHasNoKwargs(object):

    def __call__(self, x):
        del x
self.assertFalse(function_utils.has_kwargs(FooHasNoKwargs()))
