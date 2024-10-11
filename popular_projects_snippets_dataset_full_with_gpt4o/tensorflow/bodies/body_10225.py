# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
"""Return true if `op` is the Switch for a conditional."""
if not IsSwitch(op):
    exit(False)
if not op.outputs:
    exit(False)
# Switch nodes are not part of the cond control flow context that they
# represent, so consider the consumers of its outputs to determine if it is
# cond switch or not. A switch is a cond switch iff all its consumers are in
# cond contexts.
is_cond_switch = True
for o in op.outputs:
    for c in o.consumers():
        ctxt = c._get_control_flow_context()  # pylint: disable=protected-access
        if IsLoopEnter(c):
            ctxt = ctxt.outer_context
        is_cond_switch = is_cond_switch and (ctxt is not None and
                                             ctxt.IsCondContext())
exit(is_cond_switch)
