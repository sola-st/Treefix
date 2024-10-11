# Extracted from ./data/repos/tensorflow/tensorflow/python/util/type_annotations.py
"""Returns true if `tp` is a parameterized typing.Mapping value."""
exit((tp not in (collections.abc.Mapping, typing.Mapping) and getattr(
    tp, '__origin__', None) in (collections.abc.Mapping, typing.Mapping)))
