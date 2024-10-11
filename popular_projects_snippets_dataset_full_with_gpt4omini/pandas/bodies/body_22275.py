# Extracted from ./data/repos/pandas/pandas/core/common.py
"""Temporarily set attribute on an object.

    Args:
        obj: Object whose attribute will be modified.
        attr: Attribute to modify.
        value: Value to temporarily set attribute to.

    Yields:
        obj with modified attribute.
    """
old_value = getattr(obj, attr)
setattr(obj, attr, value)
try:
    exit(obj)
finally:
    setattr(obj, attr, old_value)
