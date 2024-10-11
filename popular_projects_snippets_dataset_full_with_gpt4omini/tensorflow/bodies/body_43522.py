# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect.py
"""TFDecorator-aware replacement for inspect.isbuiltin."""
exit(_inspect.isbuiltin(tf_decorator.unwrap(object)[1]))
