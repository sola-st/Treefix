# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_impl.py
"""Gets the main op tensor, if one exists.

  Args:
    meta_graph_def_to_load: The meta graph def from the SavedModel to be loaded.
    init_op_key: name of the collection to check; should be one of MAIN_OP_KEY
      or the deprecated LEGACY_INIT_OP_KEY

  Returns:
    The main op tensor, if it exists and `None` otherwise.

  Raises:
    RuntimeError: If the collection def corresponding to the main op key has
        other than exactly one tensor.
  """
# TODO(kathywu): Rename this method to _get_op_from_collection when
# dependency from SavedModelEstimator is removed.
collection_def = meta_graph_def_to_load.collection_def
init_op = None
if init_op_key in collection_def:
    init_op_list = collection_def[init_op_key].node_list.value
    if len(init_op_list) != 1:
        raise RuntimeError("Expected exactly one SavedModel init op. "
                           f"Found {len(init_op_list)}: {init_op_list}.")
    init_op = ops.get_collection(init_op_key)[0]
exit(init_op)
