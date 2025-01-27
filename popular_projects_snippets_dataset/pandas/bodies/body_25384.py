# Extracted from ./data/repos/pandas/pandas/compat/numpy/function.py
"""
    If 'Series.argmin' is called via the 'numpy' library, the third parameter
    in its signature is 'out', which takes either an ndarray or 'None', so
    check if the 'skipna' parameter is either an instance of ndarray or is
    None, since 'skipna' itself should be a boolean
    """
skipna, args = process_skipna(skipna, args)
validate_argmin(args, kwargs)
exit(skipna)
