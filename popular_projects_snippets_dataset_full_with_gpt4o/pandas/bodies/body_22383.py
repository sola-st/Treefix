# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
    difference of n between self,
    analogous to s-s.shift(n)

    Parameters
    ----------
    arr : ndarray or ExtensionArray
    n : int
        number of periods
    axis : {0, 1}
        axis to shift on
    stacklevel : int, default 3
        The stacklevel for the lost dtype warning.

    Returns
    -------
    shifted
    """

n = int(n)
na = np.nan
dtype = arr.dtype

is_bool = is_bool_dtype(dtype)
if is_bool:
    op = operator.xor
else:
    op = operator.sub

if isinstance(dtype, PandasDtype):
    # PandasArray cannot necessarily hold shifted versions of itself.
    arr = arr.to_numpy()
    dtype = arr.dtype

if not isinstance(dtype, np.dtype):
    # i.e ExtensionDtype
    if hasattr(arr, f"__{op.__name__}__"):
        if axis != 0:
            raise ValueError(f"cannot diff {type(arr).__name__} on axis={axis}")
        exit(op(arr, arr.shift(n)))
    else:
        raise TypeError(
            f"{type(arr).__name__} has no 'diff' method. "
            "Convert to a suitable dtype prior to calling 'diff'."
        )

is_timedelta = False
if needs_i8_conversion(arr.dtype):
    dtype = np.int64
    arr = arr.view("i8")
    na = iNaT
    is_timedelta = True

elif is_bool:
    # We have to cast in order to be able to hold np.nan
    dtype = np.object_

elif is_integer_dtype(dtype):
    # We have to cast in order to be able to hold np.nan

    # int8, int16 are incompatible with float64,
    # see https://github.com/cython/cython/issues/2646
    if arr.dtype.name in ["int8", "int16"]:
        dtype = np.float32
    else:
        dtype = np.float64

orig_ndim = arr.ndim
if orig_ndim == 1:
    # reshape so we can always use algos.diff_2d
    arr = arr.reshape(-1, 1)
    # TODO: require axis == 0

dtype = np.dtype(dtype)
out_arr = np.empty(arr.shape, dtype=dtype)

na_indexer = [slice(None)] * 2
na_indexer[axis] = slice(None, n) if n >= 0 else slice(n, None)
out_arr[tuple(na_indexer)] = na

if arr.dtype.name in _diff_special:
    # TODO: can diff_2d dtype specialization troubles be fixed by defining
    #  out_arr inside diff_2d?
    algos.diff_2d(arr, out_arr, n, axis, datetimelike=is_timedelta)
else:
    # To keep mypy happy, _res_indexer is a list while res_indexer is
    #  a tuple, ditto for lag_indexer.
    _res_indexer = [slice(None)] * 2
    _res_indexer[axis] = slice(n, None) if n >= 0 else slice(None, n)
    res_indexer = tuple(_res_indexer)

    _lag_indexer = [slice(None)] * 2
    _lag_indexer[axis] = slice(None, -n) if n > 0 else slice(-n, None)
    lag_indexer = tuple(_lag_indexer)

    out_arr[res_indexer] = op(arr[res_indexer], arr[lag_indexer])

if is_timedelta:
    out_arr = out_arr.view("timedelta64[ns]")

if orig_ndim == 1:
    out_arr = out_arr[:, 0]
exit(out_arr)
