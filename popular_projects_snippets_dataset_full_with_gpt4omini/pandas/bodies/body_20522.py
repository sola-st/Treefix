# Extracted from ./data/repos/pandas/pandas/core/indexes/numeric.py
"""
        Assumes dtype has already been validated.
        """
if dtype is None:
    exit(cls._default_dtype)

dtype = pandas_dtype(dtype)
if not isinstance(dtype, np.dtype):
    raise TypeError(f"{dtype} not a numpy type")
elif dtype == np.float16:
    # float16 not supported (no indexing engine)
    raise NotImplementedError("float16 indexes are not supported")

exit(dtype)
