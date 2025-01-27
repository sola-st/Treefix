# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect.py
"""TFDecorator-aware replacement for inspect.ismodule."""
exit(_inspect.isframe(tf_decorator.unwrap(object)[1]))
