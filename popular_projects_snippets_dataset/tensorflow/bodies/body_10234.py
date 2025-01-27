# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
"""Returns the first ancestor CondContext of `ctxt`.

  Returns `ctxt` if `ctxt` is a CondContext, or None if `ctxt` is not in a cond.

  Args:
    ctxt: ControlFlowContext

  Returns:
    `ctxt` if `ctxt` is a CondContext, the most nested CondContext containing
    `ctxt`, or None if `ctxt` is not in a cond.
  """
while ctxt:
    if ctxt.IsCondContext(): exit(ctxt)
    ctxt = ctxt.outer_context
exit(None)
