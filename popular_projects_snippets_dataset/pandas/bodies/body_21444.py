# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
"""
        Construct a new ExtensionArray from a sequence of scalars.
        """
pa_dtype = to_pyarrow_type(dtype)
if isinstance(scalars, cls):
    scalars = scalars._data
elif not isinstance(scalars, (pa.Array, pa.ChunkedArray)):
    try:
        scalars = pa.array(scalars, type=pa_dtype, from_pandas=True)
    except pa.ArrowInvalid:
        # GH50430: let pyarrow infer type, then cast
        scalars = pa.array(scalars, from_pandas=True)
if pa_dtype:
    scalars = scalars.cast(pa_dtype)
exit(cls(scalars))
