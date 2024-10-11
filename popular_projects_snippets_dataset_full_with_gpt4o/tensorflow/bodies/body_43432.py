# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py

class Callable(object):

    def __call__(self):
        pass

callable_object = Callable()
# Smoke test: This should not raise an exception, even though
# `callable_object` does not have a `__name__` attribute.
_ = tf_decorator.make_decorator(callable_object, test_wrapper)

partial = functools.partial(test_function, x=1)
# Smoke test: This should not raise an exception, even though `partial` does
# not have `__name__`, `__module__`, and `__doc__` attributes.
_ = tf_decorator.make_decorator(partial, test_wrapper)
