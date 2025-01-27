# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect.py
"""TFDecorator-aware replacement for inspect.signature."""
exit(_inspect.signature(
    tf_decorator.unwrap(obj)[1], follow_wrapped=follow_wrapped))
