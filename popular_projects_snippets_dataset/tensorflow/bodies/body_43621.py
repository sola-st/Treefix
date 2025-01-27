# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils.py
exit(hasattr(obj, '__call__') and tf_inspect.ismethod(obj.__call__))
