# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
    Compute a histogram of the counts of non-null values.

    Parameters
    ----------
    values : ndarray (1-d)
    sort : bool, default True
        Sort by values
    ascending : bool, default False
        Sort in ascending order
    normalize: bool, default False
        If True then compute a relative histogram
    bins : integer, optional
        Rather than count values, group them into half-open bins,
        convenience for pd.cut, only works with numeric data
    dropna : bool, default True
        Don't include counts of NaN

    Returns
    -------
    Series
    """
from pandas import (
    Index,
    Series,
)

name = getattr(values, "name", None)

if bins is not None:
    from pandas.core.reshape.tile import cut

    values = Series(values)
    try:
        ii = cut(values, bins, include_lowest=True)
    except TypeError as err:
        raise TypeError("bins argument only works with numeric data.") from err

    # count, remove nulls (from the index), and but the bins
    result = ii.value_counts(dropna=dropna)
    result = result[result.index.notna()]
    result.index = result.index.astype("interval")
    result = result.sort_index()

    # if we are dropna and we have NO values
    if dropna and (result._values == 0).all():
        result = result.iloc[0:0]

    # normalizing is by len of all (regardless of dropna)
    counts = np.array([len(ii)])

else:

    if is_extension_array_dtype(values):

        # handle Categorical and sparse,
        result = Series(values)._values.value_counts(dropna=dropna)
        result.name = name
        counts = result._values

    elif isinstance(values, ABCMultiIndex):
        # GH49558
        levels = list(range(values.nlevels))
        result = Series(index=values).groupby(level=levels, dropna=dropna).size()
        # TODO: allow index names to remain (see discussion in GH49497)
        result.index.names = [None] * values.nlevels
        counts = result._values

    else:
        values = _ensure_arraylike(values)
        keys, counts = value_counts_arraylike(values, dropna)
        if keys.dtype == np.float16:
            keys = keys.astype(np.float32)

        # For backwards compatibility, we let Index do its normal type
        #  inference, _except_ for if if infers from object to bool.
        idx = Index(keys)
        if idx.dtype == bool and keys.dtype == object:
            idx = idx.astype(object)

        result = Series(counts, index=idx, name=name)

if sort:
    result = result.sort_values(ascending=ascending)

if normalize:
    result = result / counts.sum()

exit(result)
