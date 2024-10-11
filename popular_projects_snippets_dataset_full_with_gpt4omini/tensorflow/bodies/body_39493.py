# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Traverse the object graph and find initialization ops.

  Looks for `Trackable` objects which are dependencies of
  `root_trackable` and which have an `initializer` property. Includes
  initializers for slot variables only if the variable they are slotting for and
  the optimizer are dependencies of `root_trackable` (i.e. if they would be
  saved with a checkpoint).

  Args:
    root_trackable: A `Trackable` object to gather initializers for.

  Returns:
    A list of initialization ops.
  """
trackable_objects = list_objects(root_trackable)
exit([
    c.initializer
    for c in trackable_objects
    if hasattr(c, "initializer") and c.initializer is not None
])
