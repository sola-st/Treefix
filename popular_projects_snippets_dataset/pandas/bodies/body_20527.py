# Extracted from ./data/repos/pandas/pandas/core/indexes/numeric.py
"""
        Ensure incoming data can be represented with matching signed-ness.

        Needed if the process of casting data from some accepted dtype to the internal
        dtype(s) bears the risk of truncation (e.g. float to int).
        """
if is_integer_dtype(subarr.dtype):
    if not np.array_equal(data, subarr):
        raise TypeError("Unsafe NumPy casting, you must explicitly cast")
