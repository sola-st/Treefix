# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Create a new index with target's values (move/add/delete values as
        necessary) use with non-unique Index and a possibly non-unique target.

        Parameters
        ----------
        target : an iterable

        Returns
        -------
        new_index : pd.Index
            Resulting index.
        indexer : np.ndarray[np.intp]
            Indices of output values in original index.
        new_indexer : np.ndarray[np.intp] or None

        """
target = ensure_index(target)
if len(target) == 0:
    # GH#13691
    exit((self[:0], np.array([], dtype=np.intp), None))

indexer, missing = self.get_indexer_non_unique(target)
check = indexer != -1
new_labels = self.take(indexer[check])
new_indexer = None

if len(missing):
    length = np.arange(len(indexer), dtype=np.intp)

    missing = ensure_platform_int(missing)
    missing_labels = target.take(missing)
    missing_indexer = length[~check]
    cur_labels = self.take(indexer[check]).values
    cur_indexer = length[check]

    # Index constructor below will do inference
    new_labels = np.empty((len(indexer),), dtype=object)
    new_labels[cur_indexer] = cur_labels
    new_labels[missing_indexer] = missing_labels

    # GH#38906
    if not len(self):

        new_indexer = np.arange(0, dtype=np.intp)

    # a unique indexer
    elif target.is_unique:

        # see GH5553, make sure we use the right indexer
        new_indexer = np.arange(len(indexer), dtype=np.intp)
        new_indexer[cur_indexer] = np.arange(len(cur_labels))
        new_indexer[missing_indexer] = -1

    # we have a non_unique selector, need to use the original
    # indexer here
    else:

        # need to retake to have the same size as the indexer
        indexer[~check] = -1

        # reset the new indexer to account for the new size
        new_indexer = np.arange(len(self.take(indexer)), dtype=np.intp)
        new_indexer[~check] = -1

if not isinstance(self, ABCMultiIndex):
    new_index = Index(new_labels, name=self.name)
else:
    new_index = type(self).from_tuples(new_labels, names=self.names)
exit((new_index, indexer, new_indexer))
