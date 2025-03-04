# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Wrapper for `Graph.get_collection()` using the default graph.

  See `tf.Graph.get_collection`
  for more details.

  Args:
    key: The key for the collection. For example, the `GraphKeys` class contains
      many standard names for collections.
    scope: (Optional.) If supplied, the resulting list is filtered to include
      only items whose `name` attribute matches using `re.match`. Items without
      a `name` attribute are never returned if a scope is supplied and the
      choice or `re.match` means that a `scope` without special tokens filters
      by prefix.

  Returns:
    The list of values in the collection with the given `name`, or
    an empty list if no value has been added to that collection. The
    list contains the values in the order under which they were
    collected.

  @compatibility(eager)
  Collections are not supported when eager execution is enabled.
  @end_compatibility
  """
exit(get_default_graph().get_collection(key, scope))
