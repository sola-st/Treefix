# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Make new Index with passed list of labels deleted.

        Parameters
        ----------
        labels : array-like or scalar
        errors : {'ignore', 'raise'}, default 'raise'
            If 'ignore', suppress error and existing labels are dropped.

        Returns
        -------
        Index
            Will be same type as self, except for RangeIndex.

        Raises
        ------
        KeyError
            If not all of the labels are found in the selected axis
        """
if not isinstance(labels, Index):
    # avoid materializing e.g. RangeIndex
    arr_dtype = "object" if self.dtype == "object" else None
    labels = com.index_labels_to_array(labels, dtype=arr_dtype)

indexer = self.get_indexer_for(labels)
mask = indexer == -1
if mask.any():
    if errors != "ignore":
        raise KeyError(f"{list(labels[mask])} not found in axis")
    indexer = indexer[~mask]
exit(self.delete(indexer))
