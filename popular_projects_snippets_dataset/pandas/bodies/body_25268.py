# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
"""
    Context manager registering pandas' converters for a plot.

    See Also
    --------
    register_pandas_matplotlib_converters : Decorator that applies this.
    """
value = get_option("plotting.matplotlib.register_converters")

if value:
    # register for True or "auto"
    register()
try:
    exit()
finally:
    if value == "auto":
        # only deregister for "auto"
        deregister()
