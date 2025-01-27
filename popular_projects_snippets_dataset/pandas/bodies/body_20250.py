# Extracted from ./data/repos/pandas/pandas/core/missing.py
"""
    Return a masking array of same size/shape as arr
    with entries equaling any member of values_to_mask set to True

    Parameters
    ----------
    arr : ArrayLike
    values_to_mask: list, tuple, or scalar

    Returns
    -------
    np.ndarray[bool]
    """
# When called from Block.replace/replace_list, values_to_mask is a scalar
#  known to be holdable by arr.
# When called from Series._single_replace, values_to_mask is tuple or list
dtype, values_to_mask = infer_dtype_from(values_to_mask)
# error: Argument "dtype" to "array" has incompatible type "Union[dtype[Any],
# ExtensionDtype]"; expected "Union[dtype[Any], None, type, _SupportsDType, str,
# Union[Tuple[Any, int], Tuple[Any, Union[int, Sequence[int]]], List[Any],
# _DTypeDict, Tuple[Any, Any]]]"
values_to_mask = np.array(values_to_mask, dtype=dtype)  # type: ignore[arg-type]

potential_na = False
if is_object_dtype(arr):
    # pre-compute mask to avoid comparison to NA
    potential_na = True
    arr_mask = ~isna(arr)

na_mask = isna(values_to_mask)
nonna = values_to_mask[~na_mask]

# GH 21977
mask = np.zeros(arr.shape, dtype=bool)
for x in nonna:
    if is_numeric_v_string_like(arr, x):
        # GH#29553 prevent numpy deprecation warnings
        pass
    else:
        if potential_na:
            new_mask = np.zeros(arr.shape, dtype=np.bool_)
            new_mask[arr_mask] = arr[arr_mask] == x
        else:
            new_mask = arr == x

            if not isinstance(new_mask, np.ndarray):
                # usually BooleanArray
                new_mask = new_mask.to_numpy(dtype=bool, na_value=False)
        mask |= new_mask

if na_mask.any():
    mask |= isna(arr)

exit(mask)
