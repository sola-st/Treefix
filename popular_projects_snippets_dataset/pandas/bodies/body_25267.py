# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
"""
    Decorator applying pandas_converters.
    """

@functools.wraps(func)
def wrapper(*args, **kwargs):
    with pandas_converters():
        exit(func(*args, **kwargs))

exit(cast(F, wrapper))
