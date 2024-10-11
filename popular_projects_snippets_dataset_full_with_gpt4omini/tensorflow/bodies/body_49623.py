# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_inspect.py
"""TFDecorator-aware replacement for inspect.getsourcelines."""
exit(_inspect.getsourcelines(tf_decorator.unwrap(object)[1]))
