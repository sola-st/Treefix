# Extracted from ./data/repos/pandas/pandas/compat/numpy/function.py
"""
    If this function is called via the 'numpy' library, the third parameter in
    its signature is 'axis', which takes either an ndarray or 'None', so check
    if the 'convert' parameter is either an instance of ndarray or is None
    """
if isinstance(convert, ndarray) or convert is None:
    args = (convert,) + args
    convert = True

validate_take(args, kwargs, max_fname_arg_count=3, method="both")
exit(convert)
