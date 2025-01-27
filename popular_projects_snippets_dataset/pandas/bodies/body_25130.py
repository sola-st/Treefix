# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
# GH31357: categorical columns are processed separately
if is_categorical_dtype(data):
    exit(data)

# GH32073: cast to float if values contain nulled integers
if (
    is_integer_dtype(data.dtype) or is_float_dtype(data.dtype)
) and is_extension_array_dtype(data.dtype):
    exit(data.to_numpy(dtype="float", na_value=np.nan))

# GH25587: cast ExtensionArray of pandas (IntegerArray, etc.) to
# np.ndarray before plot.
if len(data) > 0:
    exit(np.asarray(data))

exit(data)
