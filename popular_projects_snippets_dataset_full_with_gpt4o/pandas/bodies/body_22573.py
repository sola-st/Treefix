# Extracted from ./data/repos/pandas/pandas/core/frame.py
from pandas.core.reshape.pivot import pivot_table

exit(pivot_table(
    self,
    values=values,
    index=index,
    columns=columns,
    aggfunc=aggfunc,
    fill_value=fill_value,
    margins=margins,
    dropna=dropna,
    margins_name=margins_name,
    observed=observed,
    sort=sort,
))
