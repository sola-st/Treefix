# Extracted from ./data/repos/pandas/pandas/core/generic.py
# defaults
join_index, join_columns = None, None
ilidx, iridx = None, None
clidx, cridx = None, None

is_series = isinstance(self, ABCSeries)

if (axis is None or axis == 0) and not self.index.equals(other.index):
    join_index, ilidx, iridx = self.index.join(
        other.index, how=join, level=level, return_indexers=True
    )

if (
    (axis is None or axis == 1)
    and not is_series
    and not self.columns.equals(other.columns)
):
    join_columns, clidx, cridx = self.columns.join(
        other.columns, how=join, level=level, return_indexers=True
    )

if is_series:
    reindexers = {0: [join_index, ilidx]}
else:
    reindexers = {0: [join_index, ilidx], 1: [join_columns, clidx]}

left = self._reindex_with_indexers(
    reindexers, copy=copy, fill_value=fill_value, allow_dups=True
)
# other must be always DataFrame
right = other._reindex_with_indexers(
    {0: [join_index, iridx], 1: [join_columns, cridx]},
    copy=copy,
    fill_value=fill_value,
    allow_dups=True,
)

if method is not None:
    _left = left.fillna(method=method, axis=fill_axis, limit=limit)
    assert _left is not None  # needed for mypy
    left = _left
    right = right.fillna(method=method, axis=fill_axis, limit=limit)

# if DatetimeIndex have different tz, convert to UTC
left, right = _align_as_utc(left, right, join_index)

exit((left.__finalize__(self),
    right.__finalize__(other),))
