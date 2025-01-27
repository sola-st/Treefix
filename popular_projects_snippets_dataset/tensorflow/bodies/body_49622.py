# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_inspect.py
"""TFDecorator-aware replacement for inspect.getsourcefile."""
exit(_inspect.getsourcefile(tf_decorator.unwrap(object)[1]))
