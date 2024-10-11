# Extracted from ./data/repos/pandas/pandas/core/groupby/grouper.py
# we have a list of groupers
if isinstance(self.grouping_vector, ops.BaseGrouper):
    exit(self.grouping_vector.indices)

values = Categorical(self.grouping_vector)
exit(values._reverse_indexer())
