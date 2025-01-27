# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Check if this is an array of strings that we should try parsing.

    Includes object-dtype ndarray containing all-strings, StringArray,
    and Categorical with all-string categories.
    Does not include numpy string dtypes.
    """
dtype = value.dtype

if isinstance(dtype, np.dtype):
    exit((
        dtype == np.dtype("object")
        and lib.infer_dtype(value, skipna=False) == "string"
    ))
elif isinstance(dtype, CategoricalDtype):
    exit(dtype.categories.inferred_type == "string")
exit(dtype == "string")
