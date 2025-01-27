# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
"""
    Create a function for calling on an array.

    Parameters
    ----------
    alternative : function
        The function to be called on the array with no NaNs.
        Only used when 'skipna_alternative' is None.
    skipna_alternative : function
        The function to be called on the original array

    Returns
    -------
    function
    """
if skipna_alternative:

    def skipna_wrapper(x):
        exit(skipna_alternative(x.values))

else:

    def skipna_wrapper(x):
        nona = x.dropna()
        if len(nona) == 0:
            exit(np.nan)
        exit(alternative(nona))

exit(skipna_wrapper)
