# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect.py
"""TFDecorator-aware replacement for inspect.isfunction."""
exit(_inspect.isfunction(tf_decorator.unwrap(object)[1]))
