# Extracted from ./data/repos/pandas/pandas/core/generic.py

is_series = isinstance(self, ABCSeries)

if (not is_series and axis is None) or axis not in [None, 0, 1]:
    raise ValueError("Must specify axis=0 or 1")

if is_series and axis == 1:
    raise ValueError("cannot align series to a series other than axis 0")

# series/series compat, other must always be a Series
if not axis:

    # equal
    if self.index.equals(other.index):
        join_index, lidx, ridx = None, None, None
    else:
        join_index, lidx, ridx = self.index.join(
            other.index, how=join, level=level, return_indexers=True
        )

    if is_series:
        left = self._reindex_indexer(join_index, lidx, copy)
    elif lidx is None or join_index is None:
        left = self.copy(deep=copy) if copy or copy is None else self
    else:
        left = self._constructor(
            self._mgr.reindex_indexer(join_index, lidx, axis=1, copy=copy)
        )

    right = other._reindex_indexer(join_index, ridx, copy)

else:

    # one has > 1 ndim
    fdata = self._mgr
    join_index = self.axes[1]
    lidx, ridx = None, None
    if not join_index.equals(other.index):
        join_index, lidx, ridx = join_index.join(
            other.index, how=join, level=level, return_indexers=True
        )

    if lidx is not None:
        bm_axis = self._get_block_manager_axis(1)
        fdata = fdata.reindex_indexer(join_index, lidx, axis=bm_axis)

    if copy and fdata is self._mgr:
        fdata = fdata.copy()

    left = self._constructor(fdata)

    if ridx is None:
        right = other.copy(deep=copy) if copy or copy is None else other
    else:
        right = other.reindex(join_index, level=level)

        # fill
fill_na = notna(fill_value) or (method is not None)
if fill_na:
    left = left.fillna(fill_value, method=method, limit=limit, axis=fill_axis)
    right = right.fillna(fill_value, method=method, limit=limit)

# if DatetimeIndex have different tz, convert to UTC
if is_series or (not is_series and axis == 0):
    left, right = _align_as_utc(left, right, join_index)

exit((left.__finalize__(self),
    right.__finalize__(other),))
