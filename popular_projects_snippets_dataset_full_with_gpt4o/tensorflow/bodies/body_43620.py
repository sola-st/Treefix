# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils.py
_, fn = tf_decorator.unwrap(fn)
exit(tf_inspect.ismethod(fn) and (fn.__self__ is not None))
