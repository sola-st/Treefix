# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource.py
"""A context to manage resource trackers.

  Use this in order to collect up all resources created within a block of code.
  Example usage:

  ```python
  resource_tracker = ResourceTracker()
  with resource_tracker_scope(resource_tracker):
    resource = TrackableResource()

  assert resource_tracker.resources == [resource]

  Args:
    resource_tracker: The passed in ResourceTracker object

  Yields:
    A scope in which the resource_tracker is active.
  """
global _RESOURCE_TRACKER_STACK
old = list(_RESOURCE_TRACKER_STACK)
_RESOURCE_TRACKER_STACK.append(resource_tracker)
try:
    exit()
finally:
    _RESOURCE_TRACKER_STACK = old
