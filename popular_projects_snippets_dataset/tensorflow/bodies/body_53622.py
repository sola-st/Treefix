# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Wrapper for `Graph.add_to_collection()` using the default graph.

  See `tf.Graph.add_to_collection`
  for more details.

  Args:
    name: The key for the collection. For example, the `GraphKeys` class
      contains many standard names for collections.
    value: The value to add to the collection.

  @compatibility(eager)
  Collections are only supported in eager when variables are created inside
  an EagerVariableStore (e.g. as part of a layer or template).
  @end_compatibility
  """
get_default_graph().add_to_collection(name, value)
