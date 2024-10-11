# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
if not isinstance(other, RangeIndex) or sort is not None:
    exit(super().symmetric_difference(other, result_name, sort))

left = self.difference(other)
right = other.difference(self)
result = left.union(right)

if result_name is not None:
    result = result.rename(result_name)
exit(result)
