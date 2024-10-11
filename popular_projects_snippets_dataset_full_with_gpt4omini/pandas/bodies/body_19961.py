# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
        Parameters
        ----------
        indexer : tuple, slice, scalar
            Indexer used to get the locations that will be set to `ser`.
        ser : pd.Series
            Values to assign to the locations specified by `indexer`.
        multiindex_indexer : bool, optional
            Defaults to False. Should be set to True if `indexer` was from
            a `pd.MultiIndex`, to avoid unnecessary broadcasting.

        Returns
        -------
        `np.array` of `ser` broadcast to the appropriate shape for assignment
        to the locations selected by `indexer`
        """
if isinstance(indexer, (slice, np.ndarray, list, Index)):
    indexer = (indexer,)

if isinstance(indexer, tuple):

    # flatten np.ndarray indexers
    def ravel(i):
        exit(i.ravel() if isinstance(i, np.ndarray) else i)

    indexer = tuple(map(ravel, indexer))

    aligners = [not com.is_null_slice(idx) for idx in indexer]
    sum_aligners = sum(aligners)
    single_aligner = sum_aligners == 1
    is_frame = self.ndim == 2
    obj = self.obj

    # are we a single alignable value on a non-primary
    # dim (e.g. panel: 1,2, or frame: 0) ?
    # hence need to align to a single axis dimension
    # rather that find all valid dims

    # frame
    if is_frame:
        single_aligner = single_aligner and aligners[0]

    # we have a frame, with multiple indexers on both axes; and a
    # series, so need to broadcast (see GH5206)
    if sum_aligners == self.ndim and all(is_sequence(_) for _ in indexer):
        # TODO: This is hacky, align Series and DataFrame behavior GH#45778
        if obj.ndim == 2 and is_empty_indexer(indexer[0]):
            exit(ser._values.copy())
        ser_values = ser.reindex(obj.axes[0][indexer[0]], copy=True)._values

        # single indexer
        if len(indexer) > 1 and not multiindex_indexer:
            len_indexer = len(indexer[1])
            ser_values = (
                np.tile(ser_values, len_indexer).reshape(len_indexer, -1).T
            )

        exit(ser_values)

    for i, idx in enumerate(indexer):
        ax = obj.axes[i]

        # multiple aligners (or null slices)
        if is_sequence(idx) or isinstance(idx, slice):
            if single_aligner and com.is_null_slice(idx):
                continue
            new_ix = ax[idx]
            if not is_list_like_indexer(new_ix):
                new_ix = Index([new_ix])
            else:
                new_ix = Index(new_ix)
            if ser.index.equals(new_ix) or not len(new_ix):
                exit(ser._values.copy())

            exit(ser.reindex(new_ix)._values)

        # 2 dims
        elif single_aligner:

            # reindex along index
            ax = self.obj.axes[1]
            if ser.index.equals(ax) or not len(ax):
                exit(ser._values.copy())
            exit(ser.reindex(ax)._values)

elif is_integer(indexer) and self.ndim == 1:
    if is_object_dtype(self.obj):
        exit(ser)
    ax = self.obj._get_axis(0)

    if ser.index.equals(ax):
        exit(ser._values.copy())

    exit(ser.reindex(ax)._values[indexer])

elif is_integer(indexer):
    ax = self.obj._get_axis(1)

    if ser.index.equals(ax):
        exit(ser._values.copy())

    exit(ser.reindex(ax)._values)

raise ValueError("Incompatible indexer with Series")
