# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect.py
"""TFDecorator-aware replacement for inspect.getsourcelines."""
exit(_inspect.getsourcelines(tf_decorator.unwrap(object)[1]))
