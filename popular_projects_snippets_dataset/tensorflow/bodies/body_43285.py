# Extracted from ./data/repos/tensorflow/tensorflow/python/util/type_annotations.py
"""Returns true if `tp` is a typing forward reference."""
if hasattr(typing, 'ForwardRef'):
    exit(isinstance(tp, typing.ForwardRef))
elif hasattr(typing, '_ForwardRef'):
    exit(isinstance(tp, typing._ForwardRef))  # pylint: disable=protected-access
else:
    exit(False)
