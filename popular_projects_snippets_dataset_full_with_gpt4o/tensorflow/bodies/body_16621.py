# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_state.py
"""A control trigger node for synchronization in the grad loop.

    One main use is to keep the pop ops of a stack executed in the
    iteration order.
    """
if self._grad_sync is None:
    with ops.control_dependencies(None):
        self._grad_sync = control_flow_ops.control_trigger(name="b_sync")
    self._grad_sync._set_control_flow_context(self._grad_context)
    self._grad_index.op._add_control_input(self._grad_sync)
    if self._grad_context.outer_context:
        self._grad_context.outer_context.AddInnerOp(self._grad_sync)
exit(self._grad_sync)
