# Extracted from ./data/repos/pandas/pandas/core/series.py
check_dict_or_set_indexers(key)
key = com.apply_if_callable(key, self)

if key is Ellipsis:
    exit(self)

key_is_scalar = is_scalar(key)
if isinstance(key, (list, tuple)):
    key = unpack_1tuple(key)

if is_integer(key) and self.index._should_fallback_to_positional:
    exit(self._values[key])

elif key_is_scalar:
    exit(self._get_value(key))

if is_hashable(key):
    # Otherwise index.get_value will raise InvalidIndexError
    try:
        # For labels that don't resolve as scalars like tuples and frozensets
        result = self._get_value(key)

        exit(result)

    except (KeyError, TypeError, InvalidIndexError):
        # InvalidIndexError for e.g. generator
        #  see test_series_getitem_corner_generator
        if isinstance(key, tuple) and isinstance(self.index, MultiIndex):
            # We still have the corner case where a tuple is a key
            # in the first level of our MultiIndex
            exit(self._get_values_tuple(key))

if is_iterator(key):
    key = list(key)

if com.is_bool_indexer(key):
    key = check_bool_indexer(self.index, key)
    key = np.asarray(key, dtype=bool)
    exit(self._get_values(key))

exit(self._get_with(key))
