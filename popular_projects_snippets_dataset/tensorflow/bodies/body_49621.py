# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_inspect.py
"""TFDecorator-aware replacement for inspect.getsource."""
exit(_inspect.getsource(tf_decorator.unwrap(object)[1]))
