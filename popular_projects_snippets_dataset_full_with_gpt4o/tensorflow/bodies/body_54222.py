# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
"""Returns the kind name in CollectionDef.

  Args:
    item: A data item.

  Returns:
    The string representation of the kind in CollectionDef.
  """
if isinstance(item, (str, bytes)):
    kind = "bytes_list"
elif isinstance(item, int):
    kind = "int64_list"
elif isinstance(item, float):
    kind = "float_list"
elif isinstance(item, Any):
    kind = "any_list"
else:
    kind = "node_list"
exit(kind)
