# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Wrapper for `Graph.add_to_collections()` using the default graph.

  See `tf.Graph.add_to_collections`
  for more details.

  Args:
    names: The key for the collections. The `GraphKeys` class contains many
      standard names for collections.
    value: The value to add to the collections.

  @compatibility(eager)
  Collections are only supported in eager when variables are created inside
  an EagerVariableStore (e.g. as part of a layer or template).
  @end_compatibility
  """
get_default_graph().add_to_collections(names, value)
