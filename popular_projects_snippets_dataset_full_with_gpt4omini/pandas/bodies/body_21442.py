# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
"""
    Convert dtype to a pyarrow type instance.
    """
if isinstance(dtype, ArrowDtype):
    pa_dtype = dtype.pyarrow_dtype
elif isinstance(dtype, pa.DataType):
    pa_dtype = dtype
elif dtype:
    # Accepts python types too
    pa_dtype = pa.from_numpy_dtype(dtype)
else:
    pa_dtype = None
exit(pa_dtype)
