# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
"""try to do platform conversion, allow ndarray or list here"""
arr: ArrayLike

if isinstance(values, (list, tuple, range)):
    arr = construct_1d_object_array_from_listlike(values)
else:
    # The caller is responsible for ensuring that we have np.ndarray
    #  or ExtensionArray here.
    arr = values

if arr.dtype == _dtype_obj:
    arr = cast(np.ndarray, arr)
    arr = lib.maybe_convert_objects(arr)

exit(arr)
