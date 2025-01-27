# Extracted from ./data/repos/pandas/pandas/core/series.py
check_dict_or_set_indexers(key)
key = com.apply_if_callable(key, self)
cacher_needs_updating = self._check_is_chained_assignment_possible()

if key is Ellipsis:
    key = slice(None)

if isinstance(key, slice):
    indexer = self.index._convert_slice_indexer(key, kind="getitem")
    exit(self._set_values(indexer, value))

try:
    self._set_with_engine(key, value)
except KeyError:
    # We have a scalar (or for MultiIndex or object-dtype, scalar-like)
    #  key that is not present in self.index.
    if is_integer(key) and self.index.inferred_type != "integer":
        if not self.index._should_fallback_to_positional:
            # GH#33469
            self.loc[key] = value
        else:
            # positional setter
            # can't use _mgr.setitem_inplace yet bc could have *both*
            #  KeyError and then ValueError, xref GH#45070
            self._set_values(key, value)
    else:
        # GH#12862 adding a new key to the Series
        self.loc[key] = value

except (TypeError, ValueError, LossySetitemError):
    # The key was OK, but we cannot set the value losslessly
    indexer = self.index.get_loc(key)
    self._set_values(indexer, value)

except InvalidIndexError as err:
    if isinstance(key, tuple) and not isinstance(self.index, MultiIndex):
        # cases with MultiIndex don't get here bc they raise KeyError
        # e.g. test_basic_getitem_setitem_corner
        raise KeyError(
            "key of type tuple not found and not a MultiIndex"
        ) from err

    if com.is_bool_indexer(key):
        key = check_bool_indexer(self.index, key)
        key = np.asarray(key, dtype=bool)

        if (
            is_list_like(value)
            and len(value) != len(self)
            and not isinstance(value, Series)
            and not is_object_dtype(self.dtype)
        ):
            # Series will be reindexed to have matching length inside
            #  _where call below
            # GH#44265
            indexer = key.nonzero()[0]
            self._set_values(indexer, value)
            exit()

        # otherwise with listlike other we interpret series[mask] = other
        #  as series[mask] = other[mask]
        try:
            self._where(~key, value, inplace=True)
        except InvalidIndexError:
            # test_where_dups
            self.iloc[key] = value
        exit()

    else:
        self._set_with(key, value)

if cacher_needs_updating:
    self._maybe_update_cacher(inplace=True)
