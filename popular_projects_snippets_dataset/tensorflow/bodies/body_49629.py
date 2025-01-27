# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_inspect.py
"""TFDecorator-aware replacement for inspect.isgeneratorfunction."""
exit(_inspect.isgeneratorfunction(tf_decorator.unwrap(object)[1]))
