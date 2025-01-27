# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_inspect.py
"""TFDecorator-aware replacement for inspect.isroutine."""
exit(_inspect.isroutine(tf_decorator.unwrap(object)[1]))
