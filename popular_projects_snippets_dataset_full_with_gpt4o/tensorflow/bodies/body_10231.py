# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
"""Return the control flow context for the output of an op."""
ctxt = op._get_control_flow_context()  # pylint: disable=protected-access
# Exit nodes usually have a control flow context, except in the case where the
# exit node was imported via import_graph_def (in which case no nodes have
# control flow contexts).
if ctxt is not None and IsLoopExit(op):
    ctxt = ctxt.outer_context
exit(ctxt)
