# Extracted from ./data/repos/pandas/pandas/core/series.py
# other: fancy integer or otherwise
if isinstance(key, slice):
    # _convert_slice_indexer to determine if this slice is positional
    #  or label based, and if the latter, convert to positional
    slobj = self.index._convert_slice_indexer(key, kind="getitem")
    exit(self._slice(slobj))
elif isinstance(key, ABCDataFrame):
    raise TypeError(
        "Indexing a Series with DataFrame is not "
        "supported, use the appropriate DataFrame column"
    )
elif isinstance(key, tuple):
    exit(self._get_values_tuple(key))

elif not is_list_like(key):
    # e.g. scalars that aren't recognized by lib.is_scalar, GH#32684
    exit(self.loc[key])

if not isinstance(key, (list, np.ndarray, ExtensionArray, Series, Index)):
    key = list(key)

if isinstance(key, Index):
    key_type = key.inferred_type
else:
    key_type = lib.infer_dtype(key, skipna=False)

# Note: The key_type == "boolean" case should be caught by the
#  com.is_bool_indexer check in __getitem__
if key_type == "integer":
    # We need to decide whether to treat this as a positional indexer
    #  (i.e. self.iloc) or label-based (i.e. self.loc)
    if not self.index._should_fallback_to_positional:
        exit(self.loc[key])
    else:
        exit(self.iloc[key])

        # handle the dup indexing case GH#4246
exit(self.loc[key])
