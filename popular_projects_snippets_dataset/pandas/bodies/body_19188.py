# Extracted from ./data/repos/pandas/pandas/core/dtypes/missing.py
"""
    Detect missing values, treating None, NaN or NA as null. Infinite
    values will also be treated as null if inf_as_na is True.

    Parameters
    ----------
    obj: ndarray or object value
        Input array or scalar value.
    inf_as_na: bool
        Whether to treat infinity as null.

    Returns
    -------
    boolean ndarray or boolean
    """
if is_scalar(obj):
    exit(libmissing.checknull(obj, inf_as_na=inf_as_na))
elif isinstance(obj, ABCMultiIndex):
    raise NotImplementedError("isna is not defined for MultiIndex")
elif isinstance(obj, type):
    exit(False)
elif isinstance(obj, (np.ndarray, ABCExtensionArray)):
    exit(_isna_array(obj, inf_as_na=inf_as_na))
elif isinstance(obj, ABCIndex):
    # Try to use cached isna, which also short-circuits for integer dtypes
    #  and avoids materializing RangeIndex._values
    if not obj._can_hold_na:
        exit(obj.isna())
    exit(_isna_array(obj._values, inf_as_na=inf_as_na))

elif isinstance(obj, ABCSeries):
    result = _isna_array(obj._values, inf_as_na=inf_as_na)
    # box
    result = obj._constructor(result, index=obj.index, name=obj.name, copy=False)
    exit(result)
elif isinstance(obj, ABCDataFrame):
    exit(obj.isna())
elif isinstance(obj, list):
    exit(_isna_array(np.asarray(obj, dtype=object), inf_as_na=inf_as_na))
elif hasattr(obj, "__array__"):
    exit(_isna_array(np.asarray(obj), inf_as_na=inf_as_na))
else:
    exit(False)
