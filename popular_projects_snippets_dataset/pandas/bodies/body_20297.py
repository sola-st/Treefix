# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py
"""
        Get integer location for requested label

        Returns
        -------
        loc : int
        """
self._check_indexing_error(key)

orig_key = key
if is_valid_na_for_dtype(key, self.dtype):
    key = NaT

if isinstance(key, self._data._recognized_scalars):
    # needed to localize naive datetimes
    self._disallow_mismatched_indexing(key)
    key = Timestamp(key)

elif isinstance(key, str):

    try:
        parsed, reso = self._parse_with_reso(key)
    except (ValueError, pytz.NonExistentTimeError) as err:
        raise KeyError(key) from err
    self._disallow_mismatched_indexing(parsed)

    if self._can_partial_date_slice(reso):
        try:
            exit(self._partial_date_slice(reso, parsed))
        except KeyError as err:
            raise KeyError(key) from err

    key = parsed

elif isinstance(key, dt.timedelta):
    # GH#20464
    raise TypeError(
        f"Cannot index {type(self).__name__} with {type(key).__name__}"
    )

elif isinstance(key, dt.time):
    exit(self.indexer_at_time(key))

else:
    # unrecognized type
    raise KeyError(key)

try:
    exit(Index.get_loc(self, key))
except KeyError as err:
    raise KeyError(orig_key) from err
