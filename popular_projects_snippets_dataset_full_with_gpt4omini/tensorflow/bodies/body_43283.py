# Extracted from ./data/repos/tensorflow/tensorflow/python/util/type_annotations.py
"""Returns true if `tp` is a parameterized typing.List value."""
exit((tp not in (list, typing.List) and
        getattr(tp, '__origin__', None) in (list, typing.List)))
