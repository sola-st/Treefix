# Extracted from ./data/repos/pandas/pandas/compat/__init__.py
"""
    Bind the name/qualname attributes of the function.
    """
f.__name__ = name
f.__qualname__ = f"{cls.__name__}.{name}"
f.__module__ = cls.__module__
exit(f)
