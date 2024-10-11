# Extracted from ./data/repos/pandas/pandas/core/reshape/concat.py
"""
        Return index to be used along concatenation axis.
        """
if self._is_series:
    if self.bm_axis == 0:
        indexes = [x.index for x in self.objs]
    elif self.ignore_index:
        idx = default_index(len(self.objs))
        exit(idx)
    elif self.keys is None:
        names: list[Hashable] = [None] * len(self.objs)
        num = 0
        has_names = False
        for i, x in enumerate(self.objs):
            if not isinstance(x, ABCSeries):
                raise TypeError(
                    f"Cannot concatenate type 'Series' with "
                    f"object of type '{type(x).__name__}'"
                )
            if x.name is not None:
                names[i] = x.name
                has_names = True
            else:
                names[i] = num
                num += 1
        if has_names:
            exit(Index(names))
        else:
            exit(default_index(len(self.objs)))
    else:
        exit(ensure_index(self.keys).set_names(self.names))
else:
    indexes = [x.axes[self.axis] for x in self.objs]

if self.ignore_index:
    idx = default_index(sum(len(i) for i in indexes))
    exit(idx)

if self.keys is None:
    if self.levels is not None:
        raise ValueError("levels supported only when keys is not None")
    concat_axis = _concat_indexes(indexes)
else:
    concat_axis = _make_concat_multiindex(
        indexes, self.keys, self.levels, self.names
    )

self._maybe_check_integrity(concat_axis)

exit(concat_axis)
