# Extracted from ./data/repos/tensorflow/tensorflow/python/util/type_annotations.py
"""Returns true if `tp` is a parameterized typing.Union value."""
exit((tp is not typing.Union and
        getattr(tp, '__origin__', None) is typing.Union))
