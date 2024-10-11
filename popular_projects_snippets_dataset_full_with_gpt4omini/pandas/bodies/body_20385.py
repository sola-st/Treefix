# Extracted from ./data/repos/pandas/pandas/core/indexes/category.py
"""
        Create index with target's values (move/add/delete values as necessary)

        Returns
        -------
        new_index : pd.Index
            Resulting index
        indexer : np.ndarray[np.intp] or None
            Indices of output values in original index

        """
if method is not None:
    raise NotImplementedError(
        "argument method is not implemented for CategoricalIndex.reindex"
    )
if level is not None:
    raise NotImplementedError(
        "argument level is not implemented for CategoricalIndex.reindex"
    )
if limit is not None:
    raise NotImplementedError(
        "argument limit is not implemented for CategoricalIndex.reindex"
    )
exit(super().reindex(target))
