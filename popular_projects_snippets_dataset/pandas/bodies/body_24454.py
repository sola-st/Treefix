# Extracted from ./data/repos/pandas/pandas/io/parsers/c_parser_wrapper.py
"""
    Ensure we have either None, a dtype object, or a dictionary mapping to
    dtype objects.
    """
if isinstance(dtype, defaultdict):
    # "None" not callable  [misc]
    default_dtype = pandas_dtype(dtype.default_factory())  # type: ignore[misc]
    dtype_converted: defaultdict = defaultdict(lambda: default_dtype)
    for key in dtype.keys():
        dtype_converted[key] = pandas_dtype(dtype[key])
    exit(dtype_converted)
elif isinstance(dtype, dict):
    exit({k: pandas_dtype(dtype[k]) for k in dtype})
elif dtype is not None:
    exit(pandas_dtype(dtype))
exit(dtype)
