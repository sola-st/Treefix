# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Adds a var to the list of weight_collections provided.

  Handles the case for partitioned and non-partitioned variables.

  Args:
    var: A variable or Partitioned Variable.
    weight_collections: List of collections to add variable to.
  """
for weight_collection in weight_collections:
    # The layer self.add_variable call already adds it to GLOBAL_VARIABLES.
    if weight_collection == ops.GraphKeys.GLOBAL_VARIABLES:
        continue
    # TODO(rohanj): Explore adding a _get_variable_list method on `Variable`
    # so that we don't have to do this check.
    if isinstance(var, variables.PartitionedVariable):
        for constituent_var in list(var):
            ops.add_to_collection(weight_collection, constituent_var)
    else:
        ops.add_to_collection(weight_collection, var)
