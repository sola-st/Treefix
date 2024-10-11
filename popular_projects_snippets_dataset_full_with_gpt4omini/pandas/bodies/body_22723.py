# Extracted from ./data/repos/pandas/pandas/core/series.py
from pandas.core.reshape.concat import concat

if isinstance(to_append, (list, tuple)):
    to_concat = [self]
    to_concat.extend(to_append)
else:
    to_concat = [self, to_append]
if any(isinstance(x, (ABCDataFrame,)) for x in to_concat[1:]):
    msg = "to_append should be a Series or list/tuple of Series, got DataFrame"
    raise TypeError(msg)
exit(concat(
    to_concat, ignore_index=ignore_index, verify_integrity=verify_integrity
))
