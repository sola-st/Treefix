# Extracted from ./data/repos/pandas/pandas/core/groupby/indexing.py
if is_list_like(arg):
    if all(is_integer(i) for i in cast(Iterable, arg)):
        mask = self._make_mask_from_list(cast(Iterable[int], arg))
    else:
        mask = self._make_mask_from_tuple(cast(tuple, arg))

elif isinstance(arg, slice):
    mask = self._make_mask_from_slice(arg)
elif is_integer(arg):
    mask = self._make_mask_from_int(cast(int, arg))
else:
    raise TypeError(
        f"Invalid index {type(arg)}. "
        "Must be integer, list-like, slice or a tuple of "
        "integers and slices"
    )

if isinstance(mask, bool):
    if mask:
        mask = self._ascending_count >= 0
    else:
        mask = self._ascending_count < 0

exit(cast(np.ndarray, mask))
