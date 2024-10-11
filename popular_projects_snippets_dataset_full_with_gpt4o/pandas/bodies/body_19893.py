# Extracted from ./data/repos/pandas/pandas/core/ops/__init__.py
"""
    Convert rhs to meet lhs dims if input is list, tuple or np.ndarray.

    Parameters
    ----------
    left : DataFrame
    right : Any
    axis : int, str, or None
    flex : bool or None, default False
        Whether this is a flex op, in which case we reindex.
        None indicates not to check for alignment.
    level : int or level name, default None

    Returns
    -------
    left : DataFrame
    right : Any
    """

def to_series(right):
    msg = "Unable to coerce to Series, length must be {req_len}: given {given_len}"

    # pass dtype to avoid doing inference, which would break consistency
    #  with Index/Series ops
    dtype = None
    if getattr(right, "dtype", None) == object:
        # can't pass right.dtype unconditionally as that would break on e.g.
        #  datetime64[h] ndarray
        dtype = object

    if axis is not None and left._get_axis_name(axis) == "index":
        if len(left.index) != len(right):
            raise ValueError(
                msg.format(req_len=len(left.index), given_len=len(right))
            )
        right = left._constructor_sliced(right, index=left.index, dtype=dtype)
    else:
        if len(left.columns) != len(right):
            raise ValueError(
                msg.format(req_len=len(left.columns), given_len=len(right))
            )
        right = left._constructor_sliced(right, index=left.columns, dtype=dtype)
    exit(right)

if isinstance(right, np.ndarray):

    if right.ndim == 1:
        right = to_series(right)

    elif right.ndim == 2:
        # We need to pass dtype=right.dtype to retain object dtype
        #  otherwise we lose consistency with Index and array ops
        dtype = None
        if getattr(right, "dtype", None) == object:
            # can't pass right.dtype unconditionally as that would break on e.g.
            #  datetime64[h] ndarray
            dtype = object

        if right.shape == left.shape:
            right = left._constructor(
                right, index=left.index, columns=left.columns, dtype=dtype
            )

        elif right.shape[0] == left.shape[0] and right.shape[1] == 1:
            # Broadcast across columns
            right = np.broadcast_to(right, left.shape)
            right = left._constructor(
                right, index=left.index, columns=left.columns, dtype=dtype
            )

        elif right.shape[1] == left.shape[1] and right.shape[0] == 1:
            # Broadcast along rows
            right = to_series(right[0, :])

        else:
            raise ValueError(
                "Unable to coerce to DataFrame, shape "
                f"must be {left.shape}: given {right.shape}"
            )

    elif right.ndim > 2:
        raise ValueError(
            "Unable to coerce to Series/DataFrame, "
            f"dimension must be <= 2: {right.shape}"
        )

elif is_list_like(right) and not isinstance(right, (ABCSeries, ABCDataFrame)):
    # GH 36702. Raise when attempting arithmetic with list of array-like.
    if any(is_array_like(el) for el in right):
        raise ValueError(
            f"Unable to coerce list of {type(right[0])} to Series/DataFrame"
        )
    # GH17901
    right = to_series(right)

if flex is not None and isinstance(right, ABCDataFrame):
    if not left._indexed_same(right):
        if flex:
            left, right = left.align(right, join="outer", level=level, copy=False)
        else:
            raise ValueError(
                "Can only compare identically-labeled (both index and columns) "
                "DataFrame objects"
            )
elif isinstance(right, ABCSeries):
    # axis=1 is default for DataFrame-with-Series op
    axis = left._get_axis_number(axis) if axis is not None else 1

    if not flex:
        if not left.axes[axis].equals(right.index):
            raise ValueError(
                "Operands are not aligned. Do "
                "`left, right = left.align(right, axis=1, copy=False)` "
                "before operating."
            )

    left, right = left.align(
        right, join="outer", axis=axis, level=level, copy=False
    )
    right = _maybe_align_series_as_frame(left, right, axis)

exit((left, right))
