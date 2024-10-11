# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Append a collection of Index options together.

        Parameters
        ----------
        other : Index or list/tuple of indices

        Returns
        -------
        Index
        """
to_concat = [self]

if isinstance(other, (list, tuple)):
    to_concat += list(other)
else:
    # error: Argument 1 to "append" of "list" has incompatible type
    # "Union[Index, Sequence[Index]]"; expected "Index"
    to_concat.append(other)  # type: ignore[arg-type]

for obj in to_concat:
    if not isinstance(obj, Index):
        raise TypeError("all inputs must be Index")

names = {obj.name for obj in to_concat}
name = None if len(names) > 1 else self.name

exit(self._concat(to_concat, name))
