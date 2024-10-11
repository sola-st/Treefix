# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
"""Returns the first ancestor XLAContext of `ctxt`.

  Returns `ctxt` if `ctxt` is a XLAContext, or None if `ctxt` is not in a
  while loop.

  Args:
    ctxt: ControlFlowContext

  Returns:
    `ctxt` if `ctxt` is a XLAContext, the most nested XLAContext containing
    `ctxt`, or None if `ctxt` is not in a while loop.
  """
while ctxt:
    if ctxt.IsXLAContext(): exit(ctxt)
    ctxt = ctxt.outer_context
exit(None)
