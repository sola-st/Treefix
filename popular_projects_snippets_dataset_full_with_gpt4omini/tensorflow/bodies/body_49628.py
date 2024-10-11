# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_inspect.py
"""TFDecorator-aware replacement for inspect.isgenerator."""
exit(_inspect.isgenerator(tf_decorator.unwrap(object)[1]))
