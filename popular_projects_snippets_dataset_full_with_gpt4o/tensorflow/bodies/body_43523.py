# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect.py
"""TFDecorator-aware replacement for inspect.isclass."""
exit(_inspect.isclass(tf_decorator.unwrap(object)[1]))
