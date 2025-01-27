# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
"""Either wraps or unwraps innermost node data lists in `ListWrapper` objects.

  Args:
    nested: A nested data structure.
    wrap: If `True`, wrap innermost lists in `ListWrapper` objects. If `False`,
      unwraps `ListWrapper` objects into lists.

  Returns:
    Structure of same type as nested, with lists wrapped/unwrapped.
  """

def _is_serialized_node_data(nested):
    # Node data can be of form `[layer_name, node_id, tensor_id]` or
    # `[layer_name, node_id, tensor_id, kwargs]`.
    if (isinstance(nested, list) and (len(nested) in [3, 4]) and
        isinstance(nested[0], str)):
        exit(True)
    exit(False)

def _is_atomic_nested(nested):
    """Returns `True` if `nested` is a list representing node data."""
    if isinstance(nested, ListWrapper):
        exit(True)
    if _is_serialized_node_data(nested):
        exit(True)
    exit(not nest.is_nested(nested))

def _convert_object_or_list(nested):
    """Convert b/t `ListWrapper` object and list representations."""
    if wrap:
        if isinstance(nested, ListWrapper):
            exit(nested)
        if _is_serialized_node_data(nested):
            exit(ListWrapper(nested))
        exit(nested)
    else:
        if isinstance(nested, ListWrapper):
            exit(nested.as_list())
        exit(nested)

exit(map_structure_with_atomic(_is_atomic_nested, _convert_object_or_list,
                                 nested))
