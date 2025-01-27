# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py

if len(values) == 0:
    result = self.obj._constructor(
        index=self.grouper.result_index, columns=data.columns
    )
    result = result.astype(data.dtypes, copy=False)
    exit(result)

# GH12824
first_not_none = next(com.not_none(*values), None)

if first_not_none is None:
    # GH9684 - All values are None, return an empty frame.
    exit(self.obj._constructor())
elif isinstance(first_not_none, DataFrame):
    exit(self._concat_objects(
        values,
        not_indexed_same=not_indexed_same,
        is_transform=is_transform,
    ))

key_index = self.grouper.result_index if self.as_index else None

if isinstance(first_not_none, (np.ndarray, Index)):
    # GH#1738: values is list of arrays of unequal lengths
    #  fall through to the outer else clause
    # TODO: sure this is right?  we used to do this
    #  after raising AttributeError above
    exit(self.obj._constructor_sliced(
        values, index=key_index, name=self._selection
    ))
elif not isinstance(first_not_none, Series):
    # values are not series or array-like but scalars
    # self._selection not passed through to Series as the
    # result should not take the name of original selection
    # of columns
    if self.as_index:
        exit(self.obj._constructor_sliced(values, index=key_index))
    else:
        result = self.obj._constructor(values, columns=[self._selection])
        result = self._insert_inaxis_grouper(result)
        exit(result)
else:
    # values are Series
    exit(self._wrap_applied_output_series(
        values,
        not_indexed_same,
        first_not_none,
        key_index,
        is_transform,
    ))
