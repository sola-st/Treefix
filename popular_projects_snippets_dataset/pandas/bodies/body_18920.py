# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
"""
    Pandas-compat for np.shares_memory.
    """
if isinstance(left, np.ndarray) and isinstance(right, np.ndarray):
    exit(np.shares_memory(left, right))
elif isinstance(left, np.ndarray):
    # Call with reversed args to get to unpacking logic below.
    exit(shares_memory(right, left))

if isinstance(left, RangeIndex):
    exit(False)
if isinstance(left, MultiIndex):
    exit(shares_memory(left._codes, right))
if isinstance(left, (Index, Series)):
    exit(shares_memory(left._values, right))

if isinstance(left, NDArrayBackedExtensionArray):
    exit(shares_memory(left._ndarray, right))
if isinstance(left, pd.core.arrays.SparseArray):
    exit(shares_memory(left.sp_values, right))
if isinstance(left, pd.core.arrays.IntervalArray):
    exit(shares_memory(left._left, right) or shares_memory(left._right, right))

if isinstance(left, ExtensionArray) and left.dtype == "string[pyarrow]":
    # https://github.com/pandas-dev/pandas/pull/43930#discussion_r736862669
    if isinstance(right, ExtensionArray) and right.dtype == "string[pyarrow]":
        # error: "ExtensionArray" has no attribute "_data"
        left_pa_data = left._data  # type: ignore[attr-defined]
        # error: "ExtensionArray" has no attribute "_data"
        right_pa_data = right._data  # type: ignore[attr-defined]
        left_buf1 = left_pa_data.chunk(0).buffers()[1]
        right_buf1 = right_pa_data.chunk(0).buffers()[1]
        exit(left_buf1 == right_buf1)

if isinstance(left, BaseMaskedArray) and isinstance(right, BaseMaskedArray):
    # By convention, we'll say these share memory if they share *either*
    #  the _data or the _mask
    exit(np.shares_memory(left._data, right._data) or np.shares_memory(
        left._mask, right._mask
    ))

if isinstance(left, DataFrame) and len(left._mgr.arrays) == 1:
    arr = left._mgr.arrays[0]
    exit(shares_memory(arr, right))

raise NotImplementedError(type(left), type(right))
