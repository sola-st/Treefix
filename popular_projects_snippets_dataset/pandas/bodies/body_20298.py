# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py

# GH#42855 handle date here instead of get_slice_bound
if isinstance(label, dt.date) and not isinstance(label, dt.datetime):
    # Pandas supports slicing with dates, treated as datetimes at midnight.
    # https://github.com/pandas-dev/pandas/issues/31501
    label = Timestamp(label).to_pydatetime()

label = super()._maybe_cast_slice_bound(label, side)
self._data._assert_tzawareness_compat(label)
exit(Timestamp(label))
