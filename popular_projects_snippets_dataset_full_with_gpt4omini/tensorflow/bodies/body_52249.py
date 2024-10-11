# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
if isinstance(var, variables.PartitionedVariable):
    exit(list(var)[0].graph)
else:
    exit(var.graph)
