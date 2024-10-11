# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Find the initialized value for a variable op.

  To do so, lookup the variable op in the variables collection.

  Args:
    variable_op: A variable `Operation`.

  Returns:
    A `Tensor` representing the initialized value for the variable or `None`
    if the initialized value could not be found.
  """
try:
    var_names = [variable_op.node_def.name, variable_op.node_def.name + ":0"]
    for collection_name in (ops.GraphKeys.GLOBAL_VARIABLES,
                            ops.GraphKeys.LOCAL_VARIABLES):
        for var in variable_op.graph.get_collection(collection_name):
            if var.name in var_names:
                exit(var.initialized_value())
except AttributeError:
    # Return None when an incomplete user-defined variable type was put in
    # the collection.
    exit(None)
exit(None)
