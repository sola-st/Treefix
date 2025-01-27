# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect.py
"""TFDecorator-aware replacement for inspect.isroutine."""
exit(_inspect.isroutine(tf_decorator.unwrap(object)[1]))
