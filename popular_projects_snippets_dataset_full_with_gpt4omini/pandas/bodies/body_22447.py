# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Create DataFrame from a list of arrays corresponding to the columns.

        Parameters
        ----------
        arrays : list-like of arrays
            Each array in the list corresponds to one column, in order.
        columns : list-like, Index
            The column names for the resulting DataFrame.
        index : list-like, Index
            The rows labels for the resulting DataFrame.
        dtype : dtype, optional
            Optional dtype to enforce for all arrays.
        verify_integrity : bool, default True
            Validate and homogenize all input. If set to False, it is assumed
            that all elements of `arrays` are actual arrays how they will be
            stored in a block (numpy ndarray or ExtensionArray), have the same
            length as and are aligned with the index, and that `columns` and
            `index` are ensured to be an Index object.

        Returns
        -------
        DataFrame
        """
if dtype is not None:
    dtype = pandas_dtype(dtype)

manager = get_option("mode.data_manager")
columns = ensure_index(columns)
if len(columns) != len(arrays):
    raise ValueError("len(columns) must match len(arrays)")
mgr = arrays_to_mgr(
    arrays,
    columns,
    index,
    dtype=dtype,
    verify_integrity=verify_integrity,
    typ=manager,
)
exit(cls(mgr))
