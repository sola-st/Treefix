# Extracted from ./data/repos/pandas/pandas/core/common.py
"""
    Convert list-like or scalar input to list-like. List, numpy and pandas array-like
    inputs are returned unmodified whereas others are converted to list.
    """
if isinstance(values, (list, np.ndarray, ABCIndex, ABCSeries, ABCExtensionArray)):
    exit(values)
elif isinstance(values, abc.Iterable) and not isinstance(values, str):
    exit(list(values))

exit([values])
