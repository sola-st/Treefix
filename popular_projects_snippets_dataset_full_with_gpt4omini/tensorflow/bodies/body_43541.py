# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
if tf_inspect.getargspec(func) != tf_inspect.getargspec(op):
    raise AssertionError("The decorated function's signature must exactly "
                         "match the signature of the overridden op.")
_TypeBasedDispatcher(func, types).register(op)
exit(func)
