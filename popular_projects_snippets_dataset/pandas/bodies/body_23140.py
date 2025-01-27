# Extracted from ./data/repos/pandas/pandas/core/apply.py
"""
        if arg is a string, then try to operate on it:
        - try to find a function (or attribute) on ourselves
        - try to find a numpy function
        - raise
        """
assert isinstance(arg, str)

f = getattr(obj, arg, None)
if f is not None:
    if callable(f):
        exit(f(*args, **kwargs))

    # people may try to aggregate on a non-callable attribute
    # but don't let them think they can pass args to it
    assert len(args) == 0
    assert len([kwarg for kwarg in kwargs if kwarg not in ["axis"]]) == 0
    exit(f)

f = getattr(np, arg, None)
if f is not None and hasattr(obj, "__array__"):
    # in particular exclude Window
    exit(f(obj, *args, **kwargs))

raise AttributeError(
    f"'{arg}' is not a valid function for '{type(obj).__name__}' object"
)
