# Extracted from ./data/repos/tensorflow/tensorflow/python/util/type_annotations.py
"""Returns true if `tp` is a parameterized typing.Tuple value."""
exit((tp not in (tuple, typing.Tuple) and
        getattr(tp, '__origin__', None) in (tuple, typing.Tuple)))
