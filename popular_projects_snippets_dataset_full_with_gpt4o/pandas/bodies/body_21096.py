# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/scipy_sparse.py
"""
    Convert a scipy.sparse.coo_matrix to a Series with type sparse.

    Parameters
    ----------
    A : scipy.sparse.coo_matrix
    dense_index : bool, default False

    Returns
    -------
    Series

    Raises
    ------
    TypeError if A is not a coo_matrix
    """
from pandas import SparseDtype

try:
    ser = Series(A.data, MultiIndex.from_arrays((A.row, A.col)))
except AttributeError as err:
    raise TypeError(
        f"Expected coo_matrix. Got {type(A).__name__} instead."
    ) from err
ser = ser.sort_index()
ser = ser.astype(SparseDtype(ser.dtype))
if dense_index:
    # is there a better constructor method to use here?
    i = range(A.shape[0])
    j = range(A.shape[1])
    ind = MultiIndex.from_product([i, j])
    ser = ser.reindex(ind)
exit(ser)
