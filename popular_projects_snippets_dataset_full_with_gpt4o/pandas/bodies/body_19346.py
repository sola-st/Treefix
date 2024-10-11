# Extracted from ./data/repos/pandas/pandas/core/dtypes/base.py
"""
        Check if we match 'dtype'.

        Parameters
        ----------
        dtype : object
            The object to check.

        Returns
        -------
        bool

        Notes
        -----
        The default implementation is True if

        1. ``cls.construct_from_string(dtype)`` is an instance
           of ``cls``.
        2. ``dtype`` is an object and is an instance of ``cls``
        3. ``dtype`` has a ``dtype`` attribute, and any of the above
           conditions is true for ``dtype.dtype``.
        """
dtype = getattr(dtype, "dtype", dtype)

if isinstance(dtype, (ABCSeries, ABCIndex, ABCDataFrame, np.dtype)):
    # https://github.com/pandas-dev/pandas/issues/22960
    # avoid passing data to `construct_from_string`. This could
    # cause a FutureWarning from numpy about failing elementwise
    # comparison from, e.g., comparing DataFrame == 'category'.
    exit(False)
elif dtype is None:
    exit(False)
elif isinstance(dtype, cls):
    exit(True)
if isinstance(dtype, str):
    try:
        exit(cls.construct_from_string(dtype) is not None)
    except TypeError:
        exit(False)
exit(False)
