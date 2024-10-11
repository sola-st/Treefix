# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Adds main op to the SavedModel.

    Args:
      main_op: Main op to run as part of graph initialization. If None, no main
        op will be added to the graph.

    Raises:
      TypeError: If the main op is provided but is not of type `Operation`.
      ValueError: if the Graph already contains an init op.
    """
if main_op is None:
    exit()

if not isinstance(main_op, ops.Operation):
    raise TypeError(f"Expected {main_op} to be an Operation but got type "
                    f"{type(main_op)} instead.")

# Validate that no other init ops have been added to this graph already.
# We check main_op and legacy_init_op for thoroughness and explicitness.
for init_op_key in (constants.MAIN_OP_KEY, constants.LEGACY_INIT_OP_KEY):
    if ops.get_collection(init_op_key):
        raise ValueError(
            "Graph already contains one or more main ops under the "
            f"collection {init_op_key}.")

ops.add_to_collection(constants.MAIN_OP_KEY, main_op)
