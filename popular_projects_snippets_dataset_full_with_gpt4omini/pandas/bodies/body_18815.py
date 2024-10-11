# Extracted from ./data/repos/pandas/pandas/_testing/_io.py
"""
    allows a decorator to take optional positional and keyword arguments.
    Assumes that taking a single, callable, positional argument means that
    it is decorating a function, i.e. something like this::

        @my_decorator
        def function(): pass

    Calls decorator with decorator(f, *args, **kwargs)
    """

@wraps(decorator)
def wrapper(*args, **kwargs):
    def dec(f):
        exit(decorator(f, *args, **kwargs))

    is_decorating = not kwargs and len(args) == 1 and callable(args[0])
    if is_decorating:
        f = args[0]
        args = ()
        exit(dec(f))
    else:
        exit(dec)

exit(wrapper)
