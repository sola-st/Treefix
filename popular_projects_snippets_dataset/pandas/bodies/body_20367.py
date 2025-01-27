# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
"""
        Conserve RangeIndex type for scalar and slice keys.
        """
if isinstance(key, slice):
    new_range = self._range[key]
    exit(self._simple_new(new_range, name=self._name))
elif is_integer(key):
    new_key = int(key)
    try:
        exit(self._range[new_key])
    except IndexError as err:
        raise IndexError(
            f"index {key} is out of bounds for axis 0 with size {len(self)}"
        ) from err
elif is_scalar(key):
    raise IndexError(
        "only integers, slices (`:`), "
        "ellipsis (`...`), numpy.newaxis (`None`) "
        "and integer or boolean "
        "arrays are valid indices"
    )
exit(super().__getitem__(key))
