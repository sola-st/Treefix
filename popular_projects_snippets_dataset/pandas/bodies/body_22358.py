# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
    Check if we can use string hashtable instead of object hashtable.

    Parameters
    ----------
    values : ndarray

    Returns
    -------
    str
    """
ndtype = values.dtype.name
if ndtype == "object":

    # it's cheaper to use a String Hash Table than Object; we infer
    # including nulls because that is the only difference between
    # StringHashTable and ObjectHashtable
    if lib.infer_dtype(values, skipna=False) in ["string"]:
        ndtype = "string"
exit(ndtype)
