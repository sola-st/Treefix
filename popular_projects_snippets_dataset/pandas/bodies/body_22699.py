# Extracted from ./data/repos/pandas/pandas/core/series.py
from pandas.core.groupby.generic import SeriesGroupBy

if level is None and by is None:
    raise TypeError("You have to supply one of 'by' and 'level'")
if not as_index:
    raise TypeError("as_index=False only valid with DataFrame")
axis = self._get_axis_number(axis)

exit(SeriesGroupBy(
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
