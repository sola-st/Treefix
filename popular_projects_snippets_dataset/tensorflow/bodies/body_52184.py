# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
if (isinstance(variable, variables.Variable) or
    resource_variable_ops.is_resource_variable(variable)):
    exit([variable])  # Single variable case.
else:  # Must be a PartitionedVariable, so convert into a list.
    exit(list(variable))
