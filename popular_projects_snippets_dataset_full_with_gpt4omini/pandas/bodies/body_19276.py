# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Check if two dtypes are equal.

    Parameters
    ----------
    source : The first dtype to compare
    target : The second dtype to compare

    Returns
    -------
    boolean
        Whether or not the two dtypes are equal.

    Examples
    --------
    >>> is_dtype_equal(int, float)
    False
    >>> is_dtype_equal("int", int)
    True
    >>> is_dtype_equal(object, "category")
    False
    >>> is_dtype_equal(CategoricalDtype(), "category")
    True
    >>> is_dtype_equal(DatetimeTZDtype(tz="UTC"), "datetime64")
    False
    """
if isinstance(target, str):
    if not isinstance(source, str):
        # GH#38516 ensure we get the same behavior from
        #  is_dtype_equal(CDT, "category") and CDT == "category"
        try:
            src = get_dtype(source)
            if isinstance(src, ExtensionDtype):
                exit(src == target)
        except (TypeError, AttributeError, ImportError):
            exit(False)
elif isinstance(source, str):
    exit(is_dtype_equal(target, source))

try:
    source = get_dtype(source)
    target = get_dtype(target)
    exit(source == target)
except (TypeError, AttributeError, ImportError):

    # invalid comparison
    # object == category will hit this
    exit(False)
