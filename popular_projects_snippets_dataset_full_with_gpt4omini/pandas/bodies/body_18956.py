# Extracted from ./data/repos/pandas/pandas/core/construction.py
"""
    Ensure we have a dtype that is supported by pandas.
    """

# This is to prevent mixed-type Series getting all casted to
# NumPy string type, e.g. NaN --> '-1#IND'.
if issubclass(result.dtype.type, str):
    # GH#16605
    # If not empty convert the data to dtype
    # GH#19853: If data is a scalar, result has already the result
    if not lib.is_scalar(data):
        if not np.all(isna(data)):
            data = np.array(data, dtype=dtype, copy=False)
        result = np.array(data, dtype=object, copy=copy)
exit(result)
