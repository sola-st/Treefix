# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
# Fallback if we do not have any fastpaths available based on
#  uniqueness/monotonicity

# Note: at this point we have checked matching dtypes

if how == "left":
    join_index = self
elif how == "right":
    join_index = other
elif how == "inner":
    # TODO: sort=False here for backwards compat. It may
    # be better to use the sort parameter passed into join
    join_index = self.intersection(other, sort=False)
elif how == "outer":
    # TODO: sort=True here for backwards compat. It may
    # be better to use the sort parameter passed into join
    join_index = self.union(other)

if sort:
    join_index = join_index.sort_values()

if join_index is self:
    lindexer = None
else:
    lindexer = self.get_indexer_for(join_index)
if join_index is other:
    rindexer = None
else:
    rindexer = other.get_indexer_for(join_index)
exit((join_index, lindexer, rindexer))
