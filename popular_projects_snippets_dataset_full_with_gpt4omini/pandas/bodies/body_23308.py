# Extracted from ./data/repos/pandas/pandas/core/reshape/concat.py
cons: Callable[..., DataFrame | Series]
sample: DataFrame | Series

# series only
if self._is_series:
    sample = cast("Series", self.objs[0])

    # stack blocks
    if self.bm_axis == 0:
        name = com.consensus_name_attr(self.objs)
        cons = sample._constructor

        arrs = [ser._values for ser in self.objs]

        res = concat_compat(arrs, axis=0)
        result = cons(res, index=self.new_axes[0], name=name, dtype=res.dtype)
        exit(result.__finalize__(self, method="concat"))

    # combine as columns in a frame
    else:
        data = dict(zip(range(len(self.objs)), self.objs))

        # GH28330 Preserves subclassed objects through concat
        cons = sample._constructor_expanddim

        index, columns = self.new_axes
        mgr = dict_to_mgr(
            data,
            index,
            None,
            copy=self.copy,
            typ=get_option("mode.data_manager"),
        )
        if using_copy_on_write() and not self.copy:
            parents = [obj._mgr for obj in self.objs]
            mgr.parent = parents  # type: ignore[union-attr]
            refs = [
                weakref.ref(obj._mgr.blocks[0])  # type: ignore[union-attr]
                for obj in self.objs
            ]
            mgr.refs = refs  # type: ignore[union-attr]
        df = cons(mgr, copy=False)
        df.columns = columns
        exit(df.__finalize__(self, method="concat"))

        # combine block managers
else:
    sample = cast("DataFrame", self.objs[0])

    mgrs_indexers = []
    for obj in self.objs:
        indexers = {}
        for ax, new_labels in enumerate(self.new_axes):
            # ::-1 to convert BlockManager ax to DataFrame ax
            if ax == self.bm_axis:
                # Suppress reindexing on concat axis
                continue

            # 1-ax to convert BlockManager axis to DataFrame axis
            obj_labels = obj.axes[1 - ax]
            if not new_labels.equals(obj_labels):
                indexers[ax] = obj_labels.get_indexer(new_labels)

        mgrs_indexers.append((obj._mgr, indexers))

    new_data = concatenate_managers(
        mgrs_indexers, self.new_axes, concat_axis=self.bm_axis, copy=self.copy
    )
    if not self.copy and not using_copy_on_write():
        new_data._consolidate_inplace()

    cons = sample._constructor
    exit(cons(new_data).__finalize__(self, method="concat"))
