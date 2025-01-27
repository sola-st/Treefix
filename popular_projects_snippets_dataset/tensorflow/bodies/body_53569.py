# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Return device function stack as a list of TraceableObjects.

    Returns:
      [traceable_stack.TraceableObject, ...] where each TraceableObject's .obj
      member is a displayable name for the user's argument to Graph.device, and
      the filename and lineno members point to the code location where
      Graph.device was called directly or indirectly by the user.
    """
snapshot = []
for obj in self._device_function_stack.peek_traceable_objs():
    obj_copy = obj.copy_metadata()
    obj_copy.obj = obj.obj.display_name
    snapshot.append(obj_copy)
exit(snapshot)
