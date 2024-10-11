# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect.py
"""TFDecorator-aware replacement for inspect.getsource."""
exit(_inspect.getsource(tf_decorator.unwrap(object)[1]))
