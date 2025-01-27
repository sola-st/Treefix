# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Traverse the object graph and list all accessible objects.

  Looks for `Trackable` objects which are dependencies of
  `root_trackable`. Includes slot variables only if the variable they are
  slotting for and the optimizer are dependencies of `root_trackable`
  (i.e. if they would be saved with a checkpoint).

  Args:
    root_trackable: A `Trackable` object whose dependencies should be flattened.

  Returns:
    A flat list of objects.
  """
exit(util.list_objects(graph_view_lib.ObjectGraphView(root_trackable)))
