# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
        Convert a potentially-label-based key into a positional indexer.
        """
if self.name == "loc":
    # always holds here bc iloc overrides _get_setitem_indexer
    self._ensure_listlike_indexer(key)

if isinstance(key, tuple):
    for x in key:
        check_dict_or_set_indexers(x)

if self.axis is not None:
    key = _tupleize_axis_indexer(self.ndim, self.axis, key)

ax = self.obj._get_axis(0)

if isinstance(ax, MultiIndex) and self.name != "iloc" and is_hashable(key):
    with suppress(KeyError, InvalidIndexError):
        # TypeError e.g. passed a bool
        exit(ax.get_loc(key))

if isinstance(key, tuple):
    with suppress(IndexingError):
        # suppress "Too many indexers"
        exit(self._convert_tuple(key))

if isinstance(key, range):
    # GH#45479 test_loc_setitem_range_key
    key = list(key)

exit(self._convert_to_indexer(key, axis=0))
