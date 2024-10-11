# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
# compat for numpy<1.21, in which comparing a np.dtype with an ExtensionDtype
# raises instead of returning False. Once earlier numpy versions are dropped,
# this can be simplified to `return tup[1].dtype`
dtype = tup[1].dtype

if is_1d_only_ea_dtype(dtype):
    # We know these won't be consolidated, so don't need to group these.
    # This avoids expensive comparisons of CategoricalDtype objects
    sep = id(dtype)
else:
    sep = 0

exit((sep, isinstance(dtype, np.dtype), dtype))
