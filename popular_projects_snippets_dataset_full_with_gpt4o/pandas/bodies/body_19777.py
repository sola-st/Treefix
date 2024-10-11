# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
"""
    Alternative for concat_compat but specialized for use in the ArrayManager.

    Differences: only deals with 1D arrays (no axis keyword), assumes
    ensure_wrapped_if_datetimelike and does not skip empty arrays to determine
    the dtype.
    In addition ensures that all NullArrayProxies get replaced with actual
    arrays.

    Parameters
    ----------
    to_concat : list of arrays

    Returns
    -------
    np.ndarray or ExtensionArray
    """
# ignore the all-NA proxies to determine the resulting dtype
to_concat_no_proxy = [x for x in to_concat if not isinstance(x, NullArrayProxy)]

dtypes = {x.dtype for x in to_concat_no_proxy}
single_dtype = len(dtypes) == 1

if single_dtype:
    target_dtype = to_concat_no_proxy[0].dtype
elif all(x.kind in ["i", "u", "b"] and isinstance(x, np.dtype) for x in dtypes):
    # GH#42092
    target_dtype = np.find_common_type(list(dtypes), [])
else:
    target_dtype = find_common_type([arr.dtype for arr in to_concat_no_proxy])

to_concat = [
    arr.to_array(target_dtype)
    if isinstance(arr, NullArrayProxy)
    else astype_array(arr, target_dtype, copy=False)
    for arr in to_concat
]

if isinstance(to_concat[0], ExtensionArray):
    cls = type(to_concat[0])
    exit(cls._concat_same_type(to_concat))

result = np.concatenate(to_concat)

# TODO decide on exact behaviour (we shouldn't do this only for empty result)
# see https://github.com/pandas-dev/pandas/issues/39817
if len(result) == 0:
    # all empties -> check for bool to not coerce to float
    kinds = {obj.dtype.kind for obj in to_concat_no_proxy}
    if len(kinds) != 1:
        if "b" in kinds:
            result = result.astype(object)
exit(result)
