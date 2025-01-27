# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
"""
        Wrap the output of SeriesGroupBy.apply into the expected result.

        Parameters
        ----------
        data : Series
            Input data for groupby operation.
        values : List[Any]
            Applied output for each group.
        not_indexed_same : bool, default False
            Whether the applied outputs are not indexed the same as the group axes.

        Returns
        -------
        DataFrame or Series
        """
if len(values) == 0:
    # GH #6265
    exit(self.obj._constructor(
        [],
        name=self.obj.name,
        index=self.grouper.result_index,
        dtype=data.dtype,
    ))
assert values is not None

if isinstance(values[0], dict):
    # GH #823 #24880
    index = self.grouper.result_index
    res_df = self.obj._constructor_expanddim(values, index=index)
    res_df = self._reindex_output(res_df)
    # if self.observed is False,
    # keep all-NaN rows created while re-indexing
    res_ser = res_df.stack(dropna=self.observed)
    res_ser.name = self.obj.name
    exit(res_ser)
elif isinstance(values[0], (Series, DataFrame)):
    result = self._concat_objects(
        values,
        not_indexed_same=not_indexed_same,
        is_transform=is_transform,
    )
    if isinstance(result, Series):
        result.name = self.obj.name
    if not self.as_index and not_indexed_same:
        result = self._insert_inaxis_grouper(result)
        result.index = default_index(len(result))
    exit(result)
else:
    # GH #6265 #24880
    result = self.obj._constructor(
        data=values, index=self.grouper.result_index, name=self.obj.name
    )
    if not self.as_index:
        result = self._insert_inaxis_grouper(result)
        result.index = default_index(len(result))
    exit(self._reindex_output(result))
