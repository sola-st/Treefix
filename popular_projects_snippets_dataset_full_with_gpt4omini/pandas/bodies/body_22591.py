# Extracted from ./data/repos/pandas/pandas/core/frame.py
from pandas.core.reshape.merge import merge

exit(merge(
    self,
    right,
    how=how,
    on=on,
    left_on=left_on,
    right_on=right_on,
    left_index=left_index,
    right_index=right_index,
    sort=sort,
    suffixes=suffixes,
    copy=copy,
    indicator=indicator,
    validate=validate,
))
