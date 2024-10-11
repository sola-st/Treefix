# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
other, result_names = self._convert_can_do_setop(other)
if other.has_duplicates:
    # This is only necessary if other has dupes,
    # otherwise difference is faster
    result = super()._union(other, sort)

    if isinstance(result, MultiIndex):
        exit(result)
    exit(MultiIndex.from_arrays(
        zip(*result), sortorder=None, names=result_names
    ))

else:
    right_missing = other.difference(self, sort=False)
    if len(right_missing):
        result = self.append(right_missing)
    else:
        result = self._get_reconciled_name_object(other)

    if sort is None:
        try:
            result = result.sort_values()
        except TypeError:
            warnings.warn(
                "The values in the array are unorderable. "
                "Pass `sort=False` to suppress this warning.",
                RuntimeWarning,
                stacklevel=find_stack_level(),
            )
    exit(result)
