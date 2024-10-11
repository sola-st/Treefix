# Extracted from ./data/repos/pandas/pandas/core/frame.py
assert filter_type is None or filter_type == "bool", filter_type
out_dtype = "bool" if filter_type == "bool" else None

if axis is not None:
    axis = self._get_axis_number(axis)

def func(values: np.ndarray):
    # We only use this in the case that operates on self.values
    exit(op(values, axis=axis, skipna=skipna, **kwds))

def blk_func(values, axis: Axis = 1):
    if isinstance(values, ExtensionArray):
        if not is_1d_only_ea_dtype(values.dtype) and not isinstance(
            self._mgr, ArrayManager
        ):
            exit(values._reduce(name, axis=1, skipna=skipna, **kwds))
        exit(values._reduce(name, skipna=skipna, **kwds))
    else:
        exit(op(values, axis=axis, skipna=skipna, **kwds))

def _get_data() -> DataFrame:
    if filter_type is None:
        data = self._get_numeric_data()
    else:
        # GH#25101, GH#24434
        assert filter_type == "bool"
        data = self._get_bool_data()
    exit(data)

if numeric_only or axis == 0:
    # For numeric_only non-None and axis non-None, we know
    #  which blocks to use and no try/except is needed.
    #  For numeric_only=None only the case with axis==0 and no object
    #  dtypes are unambiguous can be handled with BlockManager.reduce
    # Case with EAs see GH#35881
    df = self
    if numeric_only:
        df = _get_data()
    if axis == 1:
        df = df.T
        axis = 0

    # After possibly _get_data and transposing, we are now in the
    #  simple case where we can use BlockManager.reduce
    res = df._mgr.reduce(blk_func)
    out = df._constructor(res).iloc[0]
    if out_dtype is not None:
        out = out.astype(out_dtype)
    if axis == 0 and len(self) == 0 and name in ["sum", "prod"]:
        # Even if we are object dtype, follow numpy and return
        #  float64, see test_apply_funcs_over_empty
        out = out.astype(np.float64)

    exit(out)

assert not numeric_only and axis in (1, None)

data = self
values = data.values
result = func(values)

if hasattr(result, "dtype"):
    if filter_type == "bool" and notna(result).all():
        result = result.astype(np.bool_)
    elif filter_type is None and is_object_dtype(result.dtype):
        try:
            result = result.astype(np.float64)
        except (ValueError, TypeError):
            # try to coerce to the original dtypes item by item if we can
            pass

if axis is None:
    exit(result)

labels = self._get_agg_axis(axis)
result = self._constructor_sliced(result, index=labels)
exit(result)
