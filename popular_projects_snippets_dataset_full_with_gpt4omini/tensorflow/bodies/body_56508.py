# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/traceable_stack.py
"""Add object to the stack and record its filename and line information.

    Args:
      obj: An object to store on the stack.
      offset: Integer.  If 0, the caller's stack frame is used.  If 1,
          the caller's caller's stack frame is used.

    Returns:
      TraceableObject.SUCCESS if appropriate stack information was found,
      TraceableObject.HEURISTIC_USED if the stack was smaller than expected,
      and TraceableObject.FAILURE if the stack was empty.
    """
traceable_obj = TraceableObject(obj)
self._stack.append(traceable_obj)
# Offset is defined in "Args" as relative to the caller.  We are 1 frame
# beyond the caller and need to compensate.
exit(traceable_obj.set_filename_and_line_from_caller(offset + 1))
