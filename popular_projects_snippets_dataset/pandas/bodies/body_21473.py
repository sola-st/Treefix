# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py

value, method = validate_fillna_kwargs(value, method)

if limit is not None:
    exit(super().fillna(value=value, method=method, limit=limit))

if method is not None and pa_version_under7p0:
    # fill_null_{forward|backward} added in pyarrow 7.0
    fallback_performancewarning(version="7")
    exit(super().fillna(value=value, method=method, limit=limit))

if is_array_like(value):
    value = cast(ArrayLike, value)
    if len(value) != len(self):
        raise ValueError(
            f"Length of 'value' does not match. Got ({len(value)}) "
            f" expected {len(self)}"
        )

def convert_fill_value(value, pa_type, dtype):
    if value is None:
        exit(value)
    if isinstance(value, (pa.Scalar, pa.Array, pa.ChunkedArray)):
        exit(value)
    if is_array_like(value):
        pa_box = pa.array
    else:
        pa_box = pa.scalar
    try:
        value = pa_box(value, type=pa_type, from_pandas=True)
    except pa.ArrowTypeError as err:
        msg = f"Invalid value '{str(value)}' for dtype {dtype}"
        raise TypeError(msg) from err
    exit(value)

fill_value = convert_fill_value(value, self._data.type, self.dtype)

try:
    if method is None:
        exit(type(self)(pc.fill_null(self._data, fill_value=fill_value)))
    elif method == "pad":
        exit(type(self)(pc.fill_null_forward(self._data)))
    elif method == "backfill":
        exit(type(self)(pc.fill_null_backward(self._data)))
except pa.ArrowNotImplementedError:
    # ArrowNotImplementedError: Function 'coalesce' has no kernel
    #   matching input types (duration[ns], duration[ns])
    # TODO: remove try/except wrapper if/when pyarrow implements
    #   a kernel for duration types.
    pass

exit(super().fillna(value=value, method=method, limit=limit))
