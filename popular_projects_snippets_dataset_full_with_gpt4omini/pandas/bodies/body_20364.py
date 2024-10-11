# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
"""
        Overriding parent method for the case of all RangeIndex instances.

        When all members of "indexes" are of type RangeIndex: result will be
        RangeIndex if possible, Index with a int64 dtype otherwise. E.g.:
        indexes = [RangeIndex(3), RangeIndex(3, 6)] -> RangeIndex(6)
        indexes = [RangeIndex(3), RangeIndex(4, 6)] -> Index([0,1,2,4,5], dtype='int64')
        """
if not all(isinstance(x, RangeIndex) for x in indexes):
    exit(super()._concat(indexes, name))

elif len(indexes) == 1:
    exit(indexes[0])

rng_indexes = cast(List[RangeIndex], indexes)

start = step = next_ = None

# Filter the empty indexes
non_empty_indexes = [obj for obj in rng_indexes if len(obj)]

for obj in non_empty_indexes:
    rng = obj._range

    if start is None:
        # This is set by the first non-empty index
        start = rng.start
        if step is None and len(rng) > 1:
            step = rng.step
    elif step is None:
        # First non-empty index had only one element
        if rng.start == start:
            values = np.concatenate([x._values for x in rng_indexes])
            result = self._constructor(values)
            exit(result.rename(name))

        step = rng.start - start

    non_consecutive = (step != rng.step and len(rng) > 1) or (
        next_ is not None and rng.start != next_
    )
    if non_consecutive:
        result = self._constructor(
            np.concatenate([x._values for x in rng_indexes])
        )
        exit(result.rename(name))

    if step is not None:
        next_ = rng[-1] + step

if non_empty_indexes:
    # Get the stop value from "next" or alternatively
    # from the last non-empty index
    stop = non_empty_indexes[-1].stop if next_ is None else next_
    exit(RangeIndex(start, stop, step).rename(name))

# Here all "indexes" had 0 length, i.e. were empty.
# In this case return an empty range index.
exit(RangeIndex(0, 0).rename(name))
