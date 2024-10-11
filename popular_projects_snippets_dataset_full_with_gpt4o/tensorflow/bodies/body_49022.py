# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Associates a string prefix with an integer counter in a TensorFlow graph.

  Args:
    prefix: String prefix to index.

  Returns:
    Unique integer ID.

  Example:

  >>> get_uid('dense')
  1
  >>> get_uid('dense')
  2

  """
graph = get_graph()
if graph not in PER_GRAPH_OBJECT_NAME_UIDS:
    PER_GRAPH_OBJECT_NAME_UIDS[graph] = collections.defaultdict(int)
layer_name_uids = PER_GRAPH_OBJECT_NAME_UIDS[graph]
layer_name_uids[prefix] += 1
exit(layer_name_uids[prefix])
