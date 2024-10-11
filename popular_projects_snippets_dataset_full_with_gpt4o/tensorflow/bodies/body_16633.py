# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_state.py
"""Return the grad state for this op if it's in a forward loop context."""
if before and util.IsLoopExit(op):
    forward_ctxt = op._get_control_flow_context()  # pylint: disable=protected-access
    forward_ctxt = forward_ctxt.outer_context
    if forward_ctxt:
        forward_ctxt = forward_ctxt.GetWhileContext()
else:
    forward_ctxt = util.GetWhileContext(op)
if forward_ctxt:
    exit(self._map.get(forward_ctxt))
exit(None)
