# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
if context.executing_eagerly() or save_context.in_save_context():
    exit(self._coordinator_instance.resource_handle)
else:
    self._maybe_build_distributed_table()
    closure, spec = self.resource_handle_call_time_value()
    exit(ops.get_default_graph().capture_call_time_value(
        closure,
        spec,
        default_value=self._coordinator_instance.resource_handle))
