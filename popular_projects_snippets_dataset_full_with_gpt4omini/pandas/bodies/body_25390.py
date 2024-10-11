# Extracted from ./data/repos/pandas/pandas/compat/numpy/function.py
"""
    If this function is called via the 'numpy' library, the third parameter in
    its signature is 'dtype', which takes either a 'numpy' dtype or 'None', so
    check if the 'skipna' parameter is a boolean or not
    """
if not is_bool(skipna):
    args = (skipna,) + args
    skipna = True

validate_cum_func(args, kwargs, fname=name)
exit(skipna)
