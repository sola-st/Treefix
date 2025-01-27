# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect.py
"""TFDecorator-aware replacement for inspect.ismethod."""
exit(_inspect.ismethod(tf_decorator.unwrap(object)[1]))
