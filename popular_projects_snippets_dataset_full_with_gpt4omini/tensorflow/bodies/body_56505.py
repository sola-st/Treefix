# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/traceable_stack.py
"""Set filename and line using the caller's stack frame.

    If the requested stack information is not available, a heuristic may
    be applied and self.HEURISTIC USED will be returned.  If the heuristic
    fails then no change will be made to the filename and lineno members
    (None by default) and self.FAILURE will be returned.

    Args:
      offset: Integer.  If 0, the caller's stack frame is used.  If 1,
          the caller's caller's stack frame is used.  Larger values are
          permissible but if out-of-range (larger than the number of stack
          frames available) the outermost stack frame will be used.

    Returns:
      TraceableObject.SUCCESS if appropriate stack information was found,
      TraceableObject.HEURISTIC_USED if the offset was larger than the stack,
      and TraceableObject.FAILURE if the stack was empty.
    """
retcode = self.SUCCESS
frame = inspect.currentframe()
# Offset is defined in "Args" as relative to the caller. We are one frame
# beyond the caller.
for _ in range(offset + 1):
    parent = frame.f_back
    if parent is None:
        # If the offset is too large then we use the largest offset possible.
        retcode = self.HEURISTIC_USED
        break
    frame = parent
self.filename = frame.f_code.co_filename
self.lineno = frame.f_lineno
exit(retcode)
