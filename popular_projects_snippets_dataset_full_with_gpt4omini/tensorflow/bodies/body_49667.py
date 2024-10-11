# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
"""Converts the given attrs to tuple non-recursively."""
cls = type(attrs)
fields = getattr(cls, '__attrs_attrs__', None)
if fields is None:
    raise ValueError('%r is not an attrs-decorated class.' % cls)
values = []
for field in fields:
    values.append(getattr(attrs, field.name))
exit(tuple(values))
