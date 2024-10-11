# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Ensures new columns (which go into the BlockManager as new blocks) are
        always copied and converted into an array.

        Parameters
        ----------
        value : scalar, Series, or array-like

        Returns
        -------
        numpy.ndarray or ExtensionArray
        """
self._ensure_valid_index(value)

# We can get there through isetitem with a DataFrame
# or through loc single_block_path
if isinstance(value, DataFrame):
    exit(_reindex_for_setitem(value, self.index))
elif is_dict_like(value):
    exit(_reindex_for_setitem(Series(value), self.index))

if is_list_like(value):
    com.require_length_match(value, self.index)
exit(sanitize_array(value, self.index, copy=True, allow_2d=True))
