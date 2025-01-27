# Extracted from ./data/repos/pandas/pandas/core/frame.py
from pandas.core.groupby.generic import DataFrameGroupBy

if level is None and by is None:
    raise TypeError("You have to supply one of 'by' and 'level'")
axis = self._get_axis_number(axis)

exit(DataFrameGroupBy(
    obj=self,
    keys=by,
    axis=axis,
    level=level,
    as_index=as_index,
    sort=sort,
    group_keys=group_keys,
    observed=observed,
    dropna=dropna,
))
