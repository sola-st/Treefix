# Extracted from ./data/repos/pandas/pandas/core/groupby/indexing.py
if TYPE_CHECKING:
    groupby_self = cast(groupby.GroupBy, self)
else:
    groupby_self = self

exit(groupby_self._cumcount_array(ascending=False))
