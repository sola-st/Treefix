# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py

klass: type[GroupBy]
if isinstance(obj, Series):
    from pandas.core.groupby.generic import SeriesGroupBy

    klass = SeriesGroupBy
elif isinstance(obj, DataFrame):
    from pandas.core.groupby.generic import DataFrameGroupBy

    klass = DataFrameGroupBy
else:  # pragma: no cover
    raise TypeError(f"invalid type: {obj}")

exit(klass(
    obj=obj,
    keys=by,
    axis=axis,
    level=level,
    grouper=grouper,
    exclusions=exclusions,
    selection=selection,
    as_index=as_index,
    sort=sort,
    group_keys=group_keys,
    observed=observed,
    mutated=mutated,
    dropna=dropna,
))
