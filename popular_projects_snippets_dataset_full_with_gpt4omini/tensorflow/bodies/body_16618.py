# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_state.py
"""A control trigger node for synchronization in the forward loop.

    One main use is to keep the push ops of a stack executed in the
    iteration order.
    """
if self._forward_sync is None:
    with ops.control_dependencies(None):
        self._forward_sync = control_flow_ops.control_trigger(name="f_sync")
    self._forward_sync._set_control_flow_context(self._forward_context)
    self._forward_index.op._add_control_input(self._forward_sync)
exit(self._forward_sync)
