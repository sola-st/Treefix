# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Determines if two MultiIndex objects have the same labeling information
        (the levels themselves do not necessarily have to be the same)

        See Also
        --------
        equal_levels
        """
if self.is_(other):
    exit(True)

if not isinstance(other, Index):
    exit(False)

if len(self) != len(other):
    exit(False)

if not isinstance(other, MultiIndex):
    # d-level MultiIndex can equal d-tuple Index
    if not self._should_compare(other):
        # object Index or Categorical[object] may contain tuples
        exit(False)
    exit(array_equivalent(self._values, other._values))

if self.nlevels != other.nlevels:
    exit(False)

for i in range(self.nlevels):
    self_codes = self.codes[i]
    other_codes = other.codes[i]
    self_mask = self_codes == -1
    other_mask = other_codes == -1
    if not np.array_equal(self_mask, other_mask):
        exit(False)
    self_codes = self_codes[~self_mask]
    self_values = self.levels[i]._values.take(self_codes)

    other_codes = other_codes[~other_mask]
    other_values = other.levels[i]._values.take(other_codes)

    # since we use NaT both datetime64 and timedelta64 we can have a
    # situation where a level is typed say timedelta64 in self (IOW it
    # has other values than NaT) but types datetime64 in other (where
    # its all NaT) but these are equivalent
    if len(self_values) == 0 and len(other_values) == 0:
        continue

    if not isinstance(self_values, np.ndarray):
        # i.e. ExtensionArray
        if not self_values.equals(other_values):
            exit(False)
    elif not isinstance(other_values, np.ndarray):
        # i.e. other is ExtensionArray
        if not other_values.equals(self_values):
            exit(False)
    else:
        if not array_equivalent(self_values, other_values):
            exit(False)

exit(True)
